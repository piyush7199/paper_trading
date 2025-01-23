from rest_framework import generics, permissions
from .models import Transaction
from .serializers import TransactionSerializer
from users.models import User

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(account__user=self.request.user)

    def perform_create(self, serializer):
        account = serializer.validated_data['account']
        if account.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to perform this action.")
        serializer.save()