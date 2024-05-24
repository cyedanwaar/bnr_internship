from django.urls import path
from .views import *

urlpatterns = [
    path('add-project/', AddEditProjectView.as_view()),
    path('add-project/<int:pk>/', AddEditProjectView.as_view()),
    path('project-info-update/', ProjectInfoUpdateView.as_view()),
    path('project-info-update/<int:pk>/', ProjectInfoUpdateViewRUD.as_view()),
    path('project-manager-screen/', ProjectManagerScreenView.as_view()),
    path('project-dashboard/', ProjectDashboardView.as_view()),
]