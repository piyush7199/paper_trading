from django.urls import path
from .views import SystemUserListView

urlpatterns = [
    path('users/', SystemUserListView.as_view(), name='system-user-list'),
]