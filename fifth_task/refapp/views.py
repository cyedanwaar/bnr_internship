from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .serializers import ReferenceSerializer, BidderSerializer, ResourceSerializer, ActivitySerializer
from .models import Reference, BidderSupplier, Resource, ActivityDeliverable


class ReferenceView(ListCreateAPIView):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    

class ReferenceViewRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()
    lookup_field = 'pk'


class BidderView(ListCreateAPIView):
    serializer_class = BidderSerializer
    queryset = BidderSupplier.objects.all()
    

class BidderViewRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = BidderSerializer
    queryset = BidderSupplier.objects.all()
    lookup_field = 'pk'