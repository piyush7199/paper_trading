from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import SystemUser
from .serializers import SystemUserSerializer

class SystemUserListView(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = SystemUser.objects.all()
        serializer = SystemUserSerializer(users, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)