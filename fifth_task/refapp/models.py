from django.db import models


class Job(models.Model):
    job_title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.job_title

class Applicant(models.Model):
    applicant_title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.applicant_title

class Organization(models.Model):
    organization_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.organization_name

class Company(models.Model):
    company_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.company_name

class Resource(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    period = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    # General Information
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    # Client Information
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False, blank=False) # Required
    project_name = models.CharField(max_length=255, null=False, blank=False) # Required
    sol_no = models.CharField(max_length=255, null=True, blank=True)
    task_auth_no = models.CharField(max_length=255, null=True, blank=True)

    # Technical Authority
    t_auth_name = models.CharField(max_length=255, null=True, blank=True)
    t_auth_phone_no = models.CharField(max_length=15, null=True, blank=True)
    t_auth_fax_no = models.CharField(max_length=15, null=True, blank=True)
    t_auth_email = models.EmailField(max_length=255, null=True, blank=True)
    t_auth_address = models.CharField(max_length=255, null=True, blank=True)

    # Project Authority
    p_auth_name = models.CharField(max_length=255, null=True, blank=True)
    p_auth_phone_no = models.CharField(max_length=15, null=True, blank=True)
    p_auth_fax_no = models.CharField(max_length=15, null=True, blank=True)
    p_auth_email = models.EmailField(max_length=255, null=True, blank=True)
    p_auth_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.project_name + " " + self.task_auth_no

class BiderSupplier(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    partner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=False)

    # Project Information
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # Project_details_from_client_information ********
    cost = models.IntegerField(null=True, blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)

    # Activity/Deliverable
    activity_deliverable = models.CharField(max_length=255, null=True, blank=True)
    # Activity/Deliverable description and location in Reference Contract/TA Statement of Work or Reference letter ******

    def __str__(self):
        return self.company_name + " " + self.resource.name