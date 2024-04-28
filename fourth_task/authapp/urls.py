from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup.as_view()),
    path('login/', views.LoginView.as_view()),
    # path('login/', views.login),
    path('testview/', views.testview),
    path('logout/', views.logout),
]