from rest_framework.generics import(
    RetrieveAPIView,
    ListCreateAPIView,
    # RetrieveUpdateDestroyAPIView
)

# from django.http import JsonResponse
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer, DetailBlogSerializer
from rest_framework import status
from rest_framework.response import Response

# from rest_framework.decorators import permission_classes

# from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser

from .permissions import CustomPermissionForAdmin, CustomPermissionForUser, AdminOrReadOnly


class CategoryListView(ListCreateAPIView):

   

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class LCBlog(ListCreateAPIView):
    # all_blogs = Blog.objects.filter(is_public=True)

    permission_classes = [AdminOrReadOnly,]
    all_blogs = Blog.objects.all()
    queryset = all_blogs
    serializer_class = BlogSerializer

    # permission_classes = [CustomPermissionForUser]

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = BlogSerializer(queryset, many=True, context={'request':request})

    #     if queryset.exists():
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"Message": "No blogs Found"}, status=status.HTTP_204_NO_CONTENT)


# @permission_classes([CustomPermissionForUser])
# def blog_detail(request, pk):

#     blog = Blog.objects.get(pk=pk)

#     data = {
#         'blog_title': blog.blog_title,
#         'blog_description': blog.blog_description,
#         'post_date': blog.post_date
#     }

#     return JsonResponse(data)

class Show_Blog(RetrieveAPIView):

    permission_classes = [CustomPermissionForUser]

    queryset = Blog.objects.all()
    serializer_class = DetailBlogSerializer