from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from core.utils.app_contants import default_created_on
from users.models import User  # Explicitly import the User model from the users app

class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('CASH', 'Cash'),
        ('MARGIN', 'Margin'),
    ]
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('CLOSED', 'Closed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')  # Use the User model from users app
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='CASH')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    created_on = models.BigIntegerField(default=default_created_on)

    def deposit(self, amount):
        self.balance += amount
        self.save()
        self.transactions.create(transaction_type='DEPOSIT', amount=amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            self.transactions.create(transaction_type='WITHDRAWAL', amount=amount)
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        return f"{self.user.username}'s {self.account_type} Account"
    
    class Meta:
        db_table = 'accounts'