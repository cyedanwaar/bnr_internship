from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterUserSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterUser(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = {
            "body": serializer.data
        }

        admin_or_staff = serializer.validated_data.get('admin_or_staff')
        
        if admin_or_staff == 'admin':
            user_data['message'] = "Admin Created Successfully"

        elif admin_or_staff == 'staff':
            user_data['message'] = "Staff Created Successfully"

        else:
            user_data['message'] = "User Created Successfully"

            
        return Response(user_data, status=status.HTTP_201_CREATED)
    
