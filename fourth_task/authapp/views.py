from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer



# ********** Function Based Token Signup **********

# @api_view(["POST"])
# def signup(request):

#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()

#         user = User.objects.get(username=request.data['username'])
#         token = Token.objects.get(user=user)

#         serializer = UserSerializer(user)

#         data = {
#             "user": serializer.data,
#             "token": token.key
#         }

#         return Response(data, status=status.HTTP_201_CREATED)


#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ********** Class Based Token Signup **********

class signup(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username=request.data['username'])

            token, created = Token.objects.get_or_create(user=user)

            if not created:
                token.delete()
                token = Token.objects.create(user=user)
            
            response_data = {
                'user': UserSerializer(user).data,
                'token': token.key
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):

    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {
            'user': serializer.data
        }

        token, created = Token.objects.get_or_create(user=user)

        if token:
            response_data['token'] = token.key
        elif created:
            response_data['token'] = created.key
        
        return Response(response_data, status=status.HTTP_202_ACCEPTED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])

            return Response({'token': token.key})
        return Response(serializer.errors)
        

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testview(request):


    return Response("Authenticated")


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):

    request.user.auth_token.delete()

    return Response({"message": "Logged out successfully"})
