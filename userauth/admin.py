from django.contrib import admin
from userauth.models import IndeateUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class IndeateUserAdmin(UserAdmin):
    """

    """

    list_display = ('username', 'step_reached',)
    list_filter = ('step_reached',)
    fieldsets = (
        (None, {'fields':('username', 'first_name','last_name', 'email', 'step_reached')}),)

    search_fields = ('username',)

admin.site.register(IndeateUser, IndeateUserAdmin)