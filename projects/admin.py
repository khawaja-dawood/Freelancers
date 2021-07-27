from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import MyUser
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.



class UserAdminConfig(UserAdmin):
    # search facility
    search_fields = ('email', 'username', 'registration_number',)
    # sidebar filters
    list_filter = ('email', 'username', 'is_active', 'registration_number')
    # order of the users listing
    ordering = ('-date_joined',)
    # column names on users page about User_Info
    list_display = ('username', 'registration_number', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    # styling fields on user page
    fieldsets = (
        (None, {'fields': ('registration_number', 'username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'role', 'about')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # styling about field on user page
    formfield_overrides = {
        MyUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    # required fields for adding new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('registration_number', 'username', 'first_name', 'last_name', 'role', 'email',
                       'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(MyUser, UserAdminConfig)


admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)


















