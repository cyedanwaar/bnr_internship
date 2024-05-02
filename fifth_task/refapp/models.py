from django.db import models


class Job(models.Model):

    class Meta:
        db_table = "job"
        verbose_name = "job"
        verbose_name_plural = "jobs"

    job_title = models.CharField(max_length=255, null=True, blank=True)

class Applicant(models.Model):
    class Meta:
        db_table = "applicant"
        verbose_name = "applicant"
        verbose_name_plural = "applicants"

    applicant_title = models.CharField(max_length=255, null=True, blank=True)

class Organization(models.Model):
    class Meta:
        db_table = "organization"
        verbose_name = "organization"
        verbose_name_plural = "organizations"

    organization_name = models.CharField(max_length=255, null=False, blank=False)


class Reference(models.Model):
    class Meta:
        db_table = "reference"
        verbose_name = "reference"
        verbose_name_plural = "references"

    # General Information
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    # Client Information
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False, blank=False) # Required
    project_name = models.CharField(max_length=255, null=False, blank=False) # Required
    sol_no = models.CharField(max_length=255, null=True, blank=True)
    task_auth_no = models.CharField(max_length=255, null=True, blank=True)

    # Technical Authority
    technical_auth_name = models.CharField(max_length=255, null=True, blank=True)
    technical_auth_phone_no = models.CharField(max_length=15, null=True, blank=True)
    technical_auth_fax_no = models.CharField(max_length=15, null=True, blank=True)
    technical_auth_email = models.EmailField(max_length=255, null=True, blank=True)
    technical_auth_address = models.CharField(max_length=255, null=True, blank=True)

    # Project Authority
    project_auth_name = models.CharField(max_length=255, null=True, blank=True)
    project_auth_phone_no = models.CharField(max_length=15, null=True, blank=True)
    project_auth_fax_no = models.CharField(max_length=15, null=True, blank=True)
    project_auth_email = models.EmailField(max_length=255, null=True, blank=True)
    project_auth_address = models.CharField(max_length=255, null=True, blank=True)

    # Project Information
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Project_details_from_client_information ********
    cost = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
   

class BidderSupplier(models.Model):

    class Meta:
        db_table = "biddersupplier"
        verbose_name = "biddersupplier"
        verbose_name_plural = "biddersuppliers"

    company_name = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False, blank=False, related_name="company")
    partner = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=False, related_name="partner")


class Resource(models.Model):

    class Meta:
        db_table = "resource"
        verbose_name = "resource"
        verbose_name_plural = "resources"

    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    # **************************
    period = models.CharField(max_length=255, null=True, blank=True)
    # **************************
    resource_bidder = models.ForeignKey(BidderSupplier, on_delete=models.CASCADE, null=True, related_name="resources")


class ActivityDeliverable(models.Model):

    class Meta:
        db_table = "activitydeliverable"
        verbose_name = "activitydeliverable"
        verbose_name_plural = "activityderliverables"
        
    activity_title = models.CharField(max_length=255, null=True, blank=True)
    activity_description = models.TextField(max_length=2000, null=True, blank=True)
    
    activity_bidder = models.ForeignKey(BidderSupplier, on_delete=models.CASCADE, null=True, related_name="activities")