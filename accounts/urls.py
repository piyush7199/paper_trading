from django.urls import path
from .views import AccountBalanceView, AccountDepositView, AccountWithdrawView

urlpatterns = [
    path('balance/', AccountBalanceView.as_view(), name='account-balance'),
    path('deposit/', AccountDepositView.as_view(), name='account-deposit'),
    path('withdraw/', AccountWithdrawView.as_view(), name='account-withdraw'),
]