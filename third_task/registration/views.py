from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import (
    RegisterUserSerializer,
    RegisterStaffSerializer,
    RegisterAdminSerializer
)
from rest_framework.response import Response
from rest_framework import status


class RegisterUser(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = {
            "message": "User created Successfully!",
            "body": serializer.data
        }

        return Response(user_data, status=status.HTTP_201_CREATED)
    


class RegisterStaff(GenericAPIView):
    serializer_class = RegisterStaffSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        staff_data = {
            "message": "Staff user created Successfully!",
            "body": serializer.data
        }

        return Response(staff_data, status=status.HTTP_201_CREATED)



class RegisterAdmin(GenericAPIView):
    serializer_class = RegisterAdminSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        admin_data = {
            "message": "Admin user created Successfully!",
            "body": serializer.data
        }

        return Response(admin_data, status=status.HTTP_201_CREATED)