from rest_framework import serializers
from .models import Recruiter, Proposal, Opening, Partner, Job, ProjectInformation, ProjectInfoUpdate
from drf_writable_nested import WritableNestedModelSerializer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class PartnerSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = ['project_information', 'id']


class ProjectInformationSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    partners = PartnerSerializer(required=False, many=True)

    class Meta:
        model = ProjectInformation
        fields = '__all__'
    
    def create(self, validated_data):
        partner_data = validated_data.pop('partners', [])

        od_instance = ProjectInformation.objects.create(**validated_data)

        for objs in partner_data:
            Partner.objects.create(project_information=od_instance, **objs)

        return od_instance
    

class RecruiterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    recruiter_opening = ProjectInformationSerializer(required=False, many=True)
    class Meta:
        model = Recruiter
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('recruiter_opening', [])

        recruiter_instance = Recruiter.objects.create(**validated_data)

        for objs in od_data:
            ProjectInformation.objects.create(recruiter=recruiter_instance, **objs)

        return recruiter_instance


class ProposalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    proposal_opening = ProjectInformationSerializer(required=False, many=True)
    class Meta:
        model = Proposal
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('proposal_opening', [])

        proposal_instance = Proposal.objects.create(**validated_data)

        for objs in od_data:
            ProjectInformation.objects.create(proposal=proposal_instance, **objs)
        
        return proposal_instance


class OpeningSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    details = ProjectInformationSerializer(required=False, many=True)

    class Meta:
        model = Opening
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('details', [])

        opening_instance = Opening.objects.create(**validated_data)


        for od_obj in od_data:
            partners_data = od_obj.pop('partners', [])  # Access 'partners' key for each detail
            od_instance = ProjectInformation.objects.create(openings=opening_instance, **od_obj)

            for partner_obj in partners_data:
                Partner.objects.create(project_information=od_instance, **partner_obj)

        return opening_instance
    

class ProjectInformationSerializer(serializers.ModelSerializer):
    job_project_info = JobSerializer(required=False, many=True)
    project_info = OpeningSerializer(required=False, many=True)
    class Meta:
        model = ProjectInformation
        fields = '__all__'

    def create(self, validated_data):
        job_data = validated_data.pop('job_project_info', [])

        project_info_instance = ProjectInformation.objects.create(**validated_data)

        for objs in job_data:
            Job.objects.create(job_project_info = project_info_instance, **objs)
        
        return project_info_instance


class ProjectManagerScreenSerializer(serializers.ModelSerializer):

    # Top
    project_id = serializers.CharField(source="id")
    project_name = serializers.CharField(source="project_title")

    # This field is already named as project_description so we don't need to rename
    # project_description = serializers.CharField(source="project_description")

    # Center
    # They aren't connected yet with job tracking and they will be added directly in the fields list of Meta class.

    # Center Right
    technical_evaluation_check = serializers.CharField(source='technical_evaluation_for_resume')
    financial_evaluation_check = serializers.CharField(source='financial')
    security_evaluation_check = serializers.CharField(source='security')
    education_evaluation_check = serializers.CharField(source='education')
    corporate_references_check = serializers.CharField(source='corporate_references')
    candidate_references_check = serializers.CharField(source='candidate_references')
    miscellaneous_check = serializers.CharField(source='miscellaneous')


    class Meta:
        model = ProjectInformation
        fields = ['project_id', 'project_name', 'project_description', 'technical_evaluation_check', 'financial_evaluation_check', 'security_evaluation_check', 'education_evaluation_check', 'corporate_references_check', 'candidate_references_check', 'miscellaneous_check']
    

    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)
    #     new_representation = {}

    #     for field, value in representation.items():
    #         if value == ''


class ProjectDashboardSerializer(serializers.ModelSerializer):

    # Top
    project_id = serializers.CharField(source='id')
    project_name = serializers.CharField(source='project_title')

    # This field is already named as project_description so we don't need to rename
    # project_description = serializers.CharField(source="project_description")

    # Lower Top
    technical_readiness = serializers.CharField(source='technical_evaluation_for_resume')
    financial_readiness = serializers.CharField(source='financial')
    security_readiness = serializers.CharField(source='security')

    # This field is not present in Add/Edit. It can be used from UpdateProjectInfo
    language_verification = serializers.CharField(source="ProjectInfoUpdate.candidate_language_requirement")

    # This field is same as in model so we don't need to rename
    # education = serializers.CharField(source='education')
    corporate_references_readiness = serializers.CharField(source='corporate_references')
    candidate_references_check = serializers.CharField(source='candidate_references')

    # Center Right
    technical_evaluation_check = serializers.CharField(source='technical_evaluation_for_resume')
    financial_evaluation_check = serializers.CharField(source='financial')
    security_evaluation_check = serializers.CharField(source='security')
    education_evaluation_check = serializers.CharField(source='education')
    corporate_references_check = serializers.CharField(source='corporate_references')
    candidate_references_check = serializers.CharField(source='candidate_references')
    miscellaneous_check = serializers.CharField(source='miscellaneous')

    # Center Bottom
    applicant_name = serializers.CharField(source="ProjectInfoUpdate.resource_name")
    hourly_bill_rate = serializers.CharField(source="ProjectInfoUpdate.hourly_bill_rate")
    hourly_pay_rate = serializers.CharField(source="ProjectInfoUpdate.hourly_pay_rate")
    security_verified = serializers.CharField(source="ProjectInfoUpdate.security_clearance_level")
    resource_met_the_requirements = serializers.CharField(source="ProjectInfoUpdate.candidate_meets_the_mandatory")
    resource_rated_requirements = serializers.CharField(source="ProjectInfoUpdate.candidate_rated_requirement")
    candidate_references_verified = serializers.CharField(source="ProjectInfoUpdate.candidate_reference_verification")
    

    class Meta:
        model = ProjectInformation
        fields = ['project_id','project_name','project_description','technical_readiness','financial_readiness','security_readiness','language_verification','education','corporate_references_readiness','candidate_references_check','technical_evaluation_check','financial_evaluation_check','security_evaluation_check','education_evaluation_check','corporate_references_check','candidate_references_check','miscellaneous_check','applicant_name','hourly_bill_rate','hourly_pay_rate','security_verified','resource_met_the_requirements','resource_rated_requirements','candidate_references_verified']