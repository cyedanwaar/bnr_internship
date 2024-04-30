from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ReferenceSerializer, BidderSerializer
from .models import Reference


class ReferenceView(ListCreateAPIView):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    

class ReferenceViewRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    lookup_field = 'pk'


class BidderView(ListCreateAPIView):
    serializer_class = BidderSerializer
    queryset = Reference.objects.all()
    

class BidderViewRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = BidderSerializer
    queryset = Reference.objects.all()
    lookup_field = 'pk'