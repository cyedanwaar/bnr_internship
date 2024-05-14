from django.db import models
from django.core.validators import MinValueValidator
 
 
# Create your models here.
 
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


class OpeningDetail(models.Model):

    class DropDownOptions(models.TextChoices):
        NOT_STARTED = "not_started", "Not Started"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETE = "complete", "Complete"
        REVIEWED = "reviewed", "Reviewed"
        READY_TO_SUBMIT = "ready_to_submit", "Ready To Submit"
        SUBMITTED = "submitted", "Submitted"
        NA = "N/A", "N/A"
 
    class Meta:
        db_table = 'openingdetail'
        verbose_name = 'openingdetail'
        verbose_name_plural = 'openingdetails'
 
    openings = models.ForeignKey(Opening, on_delete=models.CASCADE, null=True, blank=True, related_name="details")
 
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
    miscellaneous = models.CharField(max_length=255, null=True, blank=True)
    miscellaneous_choice = models.CharField(max_length=20, default="N/A", choices=DropDownOptions.choices)


 
class Partner(models.Model): 

    class Meta:
        db_table = 'partner'
        verbose_name = 'partner'
        verbose_name_plural = 'partners'
 
    partner_name = models.CharField(max_length=255, null=True, blank=True)
    partner_address = models.CharField(max_length=255, null=True, blank=True)
    opening_details = models.ForeignKey(OpeningDetail, on_delete=models.CASCADE, null=True, blank=True, related_name="partners")

class ProjectInformation(models.Model):

    class Meta:
        db_table = 'project_information'
        verbose_name = 'project_information'
        verbose_name_plural = 'project_informations'
    project_title = models.CharField(max_length=75, null=False, blank=False)
    project_description = models.TextField(max_length=500, null=False, blank=False)

    openings = models.ForeignKey(Opening, on_delete=models.CASCADE, null=True, blank=True, related_name='project_info')

    # reference_number = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # procurement_vehicle = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # job_mode = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # job_location = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # client_company = models.ForeignKey('self', null=True, blank=True, related_name="project_info")
    # due_time = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # due_date = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # language_requirement = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")
    # clearance_required = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="project_info")


class Job(models.Model):
    class Meta:
        db_table = 'job'
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
    title = models.CharField(max_length=255, null=True, blank=True)
    job_project_info = models.ForeignKey(ProjectInformation, on_delete=models.CASCADE ,null=False, blank=False, related_name="job")
 