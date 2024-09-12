from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["pkid","id","email","username", "first_name", "last_name", "is_staff", "is_active", "is_superuser"]
    list_display_links = ['id', 'email']
    list_filter = ["email","first_name", "last_name", "is_staff", "is_superuser", "is_active"]

    fieldsets = (
        (
            _("Login credentials"), {
                "fields": ("email", "password", )
            },
        ),
        (   _("Personal information"),
            {
                "fields": ("username","first_name", "last_name",)
            },
         
        ),
        (
            _("Permissions and groups"), {
                "fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (
            _("Important dates"), 
            {
                "fields": ("last_login", "date_joined")
            },
        ),

    )

    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2", "is_active")
            },
        ),
    )

    search_fields = ["email", "first_name", "last_name"]


admin.site.register(User, UserAdmin)