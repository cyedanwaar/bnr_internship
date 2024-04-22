from django.urls import path
from .views import LCBlog, Show_Blog, CategoryListView


urlpatterns = [
    path('blog/', LCBlog.as_view()),
    path('blog_detail/<int:pk>/', Show_Blog.as_view()),
    path('category/', CategoryListView.as_view()),
]