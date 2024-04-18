from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ListCreateProductAPIView(ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'