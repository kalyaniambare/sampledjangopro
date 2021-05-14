from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.admin import UserAdmin
from core.models import User
class UserCustomeAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'address',
            'email',
            'phone_number',
            )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User,UserCustomeAdmin)