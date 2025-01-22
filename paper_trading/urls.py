from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', include('system_user.urls')),
    path('admin/', admin.site.urls),
]
