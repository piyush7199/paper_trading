from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserRegisterSerializer, UserLoginSerializer

class UserRegisterView(views.APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={
            201: UserRegisterSerializer,
            400: "Invalid input data.",
        }
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": "success",
                "user": UserRegisterSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(views.APIView):
    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={
            200: "Login successful. Returns access and refresh tokens.",
            401: "Invalid credentials.",
            400: "Invalid input data.",
        }
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "status": "success",
                    "refresh_token": str(refresh),
                    "access_token": str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "error": "Invalid credentials."
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserRefreshTokenView(views.APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['refresh_token']
        ),
        responses={
            200: openapi.Response(
                description="New access token generated.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_STRING),
                        'access_token': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: openapi.Response(
                description="Invalid refresh token.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_STRING),
                        'error': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
        }
    )
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({
                "status": "error",
                "error": "Refresh token is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({
                "status": "success",
                "access_token": access_token,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "error": "Invalid refresh token."
            }, status=status.HTTP_400_BAD_REQUEST)