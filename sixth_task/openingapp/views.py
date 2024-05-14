from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OpeningSerializer, ProjectInformationSerializer
from .models import Opening, ProjectInformation

class OpeningView(ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectInformationSerializer

class OpeningViewRUD(RetrieveUpdateDestroyAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectInformationSerializer
    lookup_field = 'pk'