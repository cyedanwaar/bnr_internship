from django.db import models
from django.core.validators import MinValueValidator

 
class Recruiter(models.Model):
    class Meta:
        db_table = 'recruiter'
        verbose_name = 'recruiter'
        verbose_name_plural = 'recruiters'
 
    title = models.CharField(max_length=255, null=True, blank=True)
 
class Proposal(models.Model):
    class Meta:
        db_table = 'proposal'
        verbose_name = 'proposal'
        verbose_name_plural = 'proposals'
 
    title = models.CharField(max_length=255, null=True, blank=True)
 
 
class Opening(models.Model):
    class Meta:
        db_table = 'opening'
        verbose_name = 'opening'
        verbose_name_plural = 'openings'
 
    no_of_openings = models.IntegerField(default=1, validators=[MinValueValidator(1)])



# Add and edit project 
class ProjectInformation(models.Model):

    class DropDownOptions(models.TextChoices):
        NOT_STARTED = "not_started", "Not Started"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETE = "complete", "Complete"
        REVIEWED = "reviewed", "Reviewed"
        READY_TO_SUBMIT = "ready_to_submit", "Ready To Submit"
        SUBMITTED = "submitted", "Submitted"
        NA = "N/A", "N/A"
 
    class Meta:
        db_table = 'project_information'
        verbose_name = 'project_information'
        verbose_name_plural = 'project_informations'
    
    project_title = models.CharField(max_length=75, null=False, blank=False)
    project_description = models.TextField(max_length=500, null=False, blank=False)
 
    openings = models.ForeignKey(Opening, on_delete=models.CASCADE, null=True, blank=True, related_name="details")


    # no_of_openings = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # reference_number = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # procurement_vehicle = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # job_mode = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # job_location = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # client_company = models.ForeignKey('self', null=True, blank=True, related_name="project_info")
    # due_time = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # due_date = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # language_requirement = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # clearance_required = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
 
    title = models.CharField(max_length=255, null=True, blank=True)
    security_requirement = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    language_requirement = models.CharField(max_length=255, null=True, blank=True)
    
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=True, blank=True, related_name="recruiter_opening")

    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, null=True, blank=True, related_name="proposal_opening")
    
    # Additional Information
    potential_resources = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(0)])

    technical_evaluation_for_resume = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    financial = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    security = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    education = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    corporate_references = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    candidate_references = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)
    miscellaneous = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)


class Job(models.Model):
    class Meta:
        db_table = 'job'
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
    title = models.CharField(max_length=255, null=True, blank=True)
    job_project_info = models.ForeignKey(ProjectInformation, on_delete=models.CASCADE ,null=False, blank=False, related_name="job")
 

class Partner(models.Model): 

    class Meta:
        db_table = 'partner'
        verbose_name = 'partner'
        verbose_name_plural = 'partners'
 
    partner_name = models.CharField(max_length=255, null=True, blank=True)
    partner_address = models.CharField(max_length=255, null=True, blank=True)
    project_information = models.ForeignKey(ProjectInformation, on_delete=models.CASCADE, null=True, blank=True, related_name="partners")


class ProjectInfoUpdate(models.Model):

    class DropDownOptionsOne(models.TextChoices):
        YES = 'yes', 'Yes'
        NO = 'no', 'No'
        NA = 'n/a', 'N/A'
    
    class DropDownOptionsTwo(models.TextChoices):
        IND = 'independent_contractor', 'Independent Contractor'
        TE = 'term_employee', 'Term Employee'
        E = 'employee', 'Employee'


    resource_name = models.CharField(max_length=255, null=False, blank=False)
    hourly_bill_rate = models.CharField(max_length=255, null=False, blank=False)
    hourly_pay_rate = models.CharField(max_length=255, null=False, blank=False)

    security_clearance_level = models.CharField(max_length=255, null=True, blank=True)
    security_clearance_expiry_date = models.DateField(null=True, blank=True)
    security_clearance_verified = models.CharField(max_length=5, choices=DropDownOptionsOne.choices, null=False, blank=False)
    security_file_number = models.IntegerField(null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    candidate_reference_verification = models.CharField(max_length=5, choices=DropDownOptionsOne.choices, null=False, blank=False)
    education_verification = models.CharField(max_length=5, choices=DropDownOptionsOne.choices, null=False, blank=False)
    candidate_employment = models.CharField(max_length=25, choices=DropDownOptionsTwo.choices, null=False, blank=False)

    candidate_meets_the_mandatory = models.CharField(max_length=5, choices=DropDownOptionsOne.choices, null=False, blank=False)
    candidate_rated_requirement = models.IntegerField(null=False, blank=False)
    candidate_language_requirement = models.CharField(max_length=5, choices=DropDownOptionsOne.choices, null=False, blank=False)

    project_details = models.OneToOneField(ProjectInformation, on_delete=models.CASCADE, null=True, blank=True, related_name='project_update_info')

class ProjectFiles(models.Model):
    class Meta:
        db_table = "project_files"
        verbose_name = "project_files"
        verbose_name_plural = "project_files"
    prepared_resume = models.FileField(null=True, blank=True)
    exclusivity_agreement = models.FileField(null=True, blank=True)
    nda = models.FileField(null=True, blank=True)
    education = models.FileField(null=True, blank=True)
    candidate_reference = models.FileField(null=True, blank=True)

    project_info_update = models.ForeignKey(ProjectInfoUpdate, on_delete=models.CASCADE, null=True, blank=True, related_name="project_files")