from rest_framework import serializers
from .models import Recruiter, Proposal, Opening, Job, ProjectInformation, ProjectInfoUpdate, ProjectFiles
from drf_writable_nested import WritableNestedModelSerializer

class ProjectInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfoUpdate
        fields = '__all__'


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
    
class ProjectInformationFields(serializers.ModelSerializer):
    project_id = serializers.CharField(source='id')
    project_name = serializers.CharField(source='project_title')
    technical_readiness = serializers.CharField(source='technical_evaluation_for_resume')
    financial_readiness = serializers.CharField(source='financial')
    security_readiness = serializers.CharField(source='security')
    corporate_references_readiness = serializers.CharField(source='corporate_references')
    candidate_references_check = serializers.CharField(source='candidate_references')

    technical_evaluation_check = serializers.CharField(source='technical_evaluation_for_resume')
    financial_evaluation_check = serializers.CharField(source='financial')
    security_evaluation_check = serializers.CharField(source='security')
    education_evaluation_check = serializers.CharField(source='education')
    corporate_references_check = serializers.CharField(source='corporate_references')
    miscellaneous_check = serializers.CharField(source='miscellaneous')

    class Meta:
        model = ProjectInformation
        fields = [
            'project_id',
            'project_name',
            'project_description',
            'technical_readiness',
            'financial_readiness',
            'security_readiness',
            'corporate_references_readiness',
            'candidate_references_check',
            'technical_evaluation_check',
            'financial_evaluation_check',
            'security_evaluation_check',
            'education_evaluation_check',
            'corporate_references_check',
            'miscellaneous_check',
        ]

class ProjectInfoUpdateFields(serializers.ModelSerializer):

    language_verification = serializers.CharField(source="candidate_language_requirement")
    applicant_name = serializers.CharField(source="resource_name")
    security_verified = serializers.CharField(source="security_clearance_level")
    resource_met_the_requirements = serializers.CharField(source="candidate_meets_the_mandatory")
    resource_rated_requirements = serializers.CharField(source="candidate_rated_requirement")
    candidate_references_verified = serializers.CharField(source="candidate_reference_verification")

    class Meta:
        model = ProjectInfoUpdate
        fields = [
            'language_verification',
            'applicant_name',
            'hourly_bill_rate',
            'hourly_pay_rate',
            'security_verified',
            'resource_met_the_requirements',
            'resource_rated_requirements',
            'candidate_references_verified',
        ]

class ProjectDashboardSerializer(serializers.ModelSerializer):
    project_details = ProjectInformationFields(source="*")
    project_update_info = ProjectInfoUpdateFields()

    class Meta:
        model = ProjectInfoUpdate
        fields = ['project_update_info', 'project_details']
    
class NoOfOpeningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opening
        fields = '__all__'


class AddEditProjectSerailizer(serializers.ModelSerializer):
    details = NoOfOpeningSerializer(required=False, many=True)
    class Meta:
        model = ProjectInformation
        fields = '__all__'
    
    def create(self, validated_data):

        details_data = validated_data.pop('details', [])
        project_info_instance = ProjectInformation.objects.create(**validated_data)

        bulk_details = [ProjectInformation(openings=details_data,**i)for i in ProjectInformation['details']]

        Opening.objects.bulk_create(bulk_details)

        return project_info_instance
    