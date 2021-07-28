from django.contrib import admin, messages
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import MyUser
from django.utils.translation import gettext_lazy as _


@admin.action(description='Inactive selected users')
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=0)
    queryset.update(is_superuser=0)
    queryset.update(is_staff=0)
    messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")


@admin.action(description='Active selected users')
def make_active(modeladmin, request, queryset):
    print(queryset.MyUser)
    print(request)
    queryset.update(is_active=1)
    messages.success(request, f"Selected Record() Marked as Active Successfully !!")


class UserAdminConfig(UserAdmin, admin.ModelAdmin):
    # list_editable = ['phone_number']

    # action list
    actions = [make_inactive, make_active]
    # search facility
    search_fields = ('email', 'username', 'registration_number', 'organization_role')
    # sidebar filters
    list_filter = ('email', 'username', 'is_active', 'registration_number', 'organization_role')
    # order of the users listing
    ordering = ('-date_joined',)
    # column names on users page about User_Info
    list_display = (
        'username', 'registration_number', 'email', 'first_name', 'last_name', 'phone_number', 'organization_role', 'is_active',
        'is_staff')
    # styling fields on user page
    fieldsets = (
        (None, {'fields': ('registration_number', 'username', 'email', 'password')}),
        (
            _('Personal info'),
            {'fields': ('first_name', 'last_name', 'phone_number', 'organization_role', 'job_title', 'about', 'tags')}),
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
            'fields': (
                'registration_number', 'username', 'first_name', 'last_name', 'phone_number', 'organization_role', 'job_title', 'email',
                'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


class ProjectAdmin(admin.ModelAdmin):
    # search facility

    # search_fields = ('title', 'developer', 'tags',)
    ordering = ('-created',)
    list_filter = ('developer', 'created')
    list_display = ('title', 'developer', 'vote_total', 'vote_ratio', 'created', 'active')


class ReviewAdmin(admin.ModelAdmin):

    ordering = ('-updated',)
    list_filter = ('value', 'project', 'author', 'created')
    list_display = ('value', 'project', 'author', 'created', 'active')


admin.site.register(MyUser, UserAdminConfig)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag)
