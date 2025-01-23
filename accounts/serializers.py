from rest_framework import serializers
from .models import Account
from users.models import User

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Account
        fields = ['id', 'user', 'account_type', 'balance', 'status', 'created_on']
        read_only_fields = ['id', 'user', 'created_on']