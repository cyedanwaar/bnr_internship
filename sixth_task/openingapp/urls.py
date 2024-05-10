from django.urls import path
from . import views

urlpatterns = [
    path('opening/', views.OpeningView.as_view()),
    path('opening/<int:pk>/', views.OpeningViewRUD.as_view()),
]