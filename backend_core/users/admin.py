from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import CustomUser

class UserAdminConfig(UserAdmin):
    model = get_user_model()
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-last_login',)
    list_display = ('email', 'username', 'is_active', 'is_staff')

admin.site.register(User, UserAdminConfig)
