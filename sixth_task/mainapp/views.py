from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import ProjectInformation, ProjectInfoUpdate
from .serializers import ProjectManagerScreenSerializer, ProjectDashboardSerializer


class ProjectManagerScreenView(ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectManagerScreenSerializer


class ProjectDashboardView(ListCreateAPIView):
    serializer_class = ProjectDashboardSerializer
    queryset = ProjectInformation.objects.all()

    # def get_queryset(self):
    #     return ProjectInformation.objects.all()


    # def get_context_data(self, **kwargs):
    #     context = super(IndexView)

        # queryset = {
        #     'project_info': ProjectInformation.objects.all(),
        #     'project_info_update': ProjectInfoUpdate.objects.all()
        # }
        
        # project_info_queryset = ProjectInformation.objects.all().values_list(
        #     'id','project_title','project_description','technical_evaluation_for_resume','financial','security','education','corporate_references','candidate_references','miscellaneous'
        # )
        # project_info_update_queryset = ProjectInfoUpdate.objects.all().values_list(
        #     'candidate_language_requirement', 'resource_name','hourly_bill_rate','hourly_pay_rate','security_clearance_level','candidate_meets_the_mandatory','candidate_rated_requirement','candidate_reference_verification',
        # )

        # return project_info_queryset.union(project_info_update_queryset)
        # return