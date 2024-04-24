from django.urls import path
from .views import (
    RegisterUser,
    RegisterStaff,
    RegisterAdmin
)


urlpatterns = [
    path('user/', RegisterUser.as_view()),
    path('staff/', RegisterStaff.as_view()),
    path('admin/', RegisterAdmin.as_view()),
]