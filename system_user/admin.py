from django.contrib import admin
from .models import SystemUser

@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')