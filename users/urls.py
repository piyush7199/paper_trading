from django.urls import path
from .views import UserRegisterView, UserLoginView, UserRefreshTokenView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('refresh-token/', UserRefreshTokenView.as_view(), name='user-refresh-token'),
]