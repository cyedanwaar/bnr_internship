from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProjectInformation, ProjectInfoUpdate, Opening
# from .serializers import ProjectManagerScreenSerializer, ProjectDashboardSerializer, OpeningSerializer, ProjectInfoUpdateSerializer
from .serializers import AddEditProjectSerailizer, ProjectDashboardSerializer, ProjectInfoUpdateSerializer, ProjectManagerScreenSerializer
from drf_multiple_model.views import FlatMultipleModelAPIView


class AddEditProjectView(ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = AddEditProjectSerailizer

class AddEditProjectViewRUD(RetrieveUpdateDestroyAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = AddEditProjectSerailizer
    lookup_field = 'pk'


class ProjectInfoUpdateView(ListCreateAPIView):
    queryset = ProjectInfoUpdate.objects.all()
    serializer_class = ProjectInfoUpdateSerializer

class ProjectInfoUpdateViewRUD(RetrieveUpdateDestroyAPIView):
    queryset = ProjectInfoUpdate.objects.all()
    serializer_class = ProjectInfoUpdateSerializer
    lookup_field = 'pk'


class ProjectManagerScreenView(ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectManagerScreenSerializer


class ProjectDashboardView(ListCreateAPIView):
    serializer_class = ProjectDashboardSerializer
    queryset = ProjectInformation.objects.all()

