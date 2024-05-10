from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OpeningSerializer
from .models import Opening

class OpeningView(ListCreateAPIView):
    queryset = Opening.objects.all()
    serializer_class = OpeningSerializer

class OpeningViewRUD(RetrieveUpdateDestroyAPIView):
    queryset = Opening.objects.all()
    serializer_class = OpeningSerializer
    lookup_field = 'pk'