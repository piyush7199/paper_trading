from rest_framework import serializers
from .models import SystemUser

class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'created_on')