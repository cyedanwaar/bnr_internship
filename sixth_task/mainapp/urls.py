from django.urls import path
from .views import ProjectManagerScreenView, ProjectDashboardView


urlpatterns = [
    path('pms/', ProjectManagerScreenView.as_view()),
    path('pdb/', ProjectDashboardView.as_view()),
]