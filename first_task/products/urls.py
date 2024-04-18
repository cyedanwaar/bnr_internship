from django.urls import path
from .views import ListCreateProductAPIView, RetrieveUpdateDestroyProductAPIView

urlpatterns = [
    path('products/', ListCreateProductAPIView.as_view()),
    path('products/', RetrieveUpdateDestroyProductAPIView.as_view()),
]