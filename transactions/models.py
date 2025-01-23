from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Account
from core.utils.app_contants import default_created_on

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.TextField(blank=True, null=True)
    timestamp = models.BigIntegerField(default=default_created_on)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"
    
    class Meta:
        db_table = 'transactions'