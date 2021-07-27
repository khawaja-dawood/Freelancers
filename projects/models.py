from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, UserManager
from django.apps import apps

from freelancer import settings


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, registration_number=None, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email_address')

        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, registration_number=registration_number, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, registration_number=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        return self._create_user(username=username, registration_number=registration_number, email=email, password=password, **extra_fields)

    def create_user(self, username, registration_number=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, registration_number=registration_number, email=email, password=password, **extra_fields)



class MyUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    registration_number = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=100, default='Student', help_text='By Default is Student. Admin, Developer, Teacher, Student')
    about = models.TextField(max_length=300, blank=True, null=True)
    is_staff = models.BooleanField(default=False,
                                   help_text='Designates whether the user can log into this admin site.',
                                   )
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. '
                                                            'Unselect this instead of deleting accounts.')
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email' """=============================+++++++++++++++++++++============================="""
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['registration_number', 'email']


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=150, on_delete=models.CASCADE, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    active = models.BooleanField(default=True)
    # Null(false) --> for database will not allow and blank(false) --> django forms will not allow submission
    # auto_now_add --> takes a timestamp when the obj is created.   auto_now --> takes a timestamp everytime the obj is updated.

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except ValueError:
            img = ''
        return img

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value + " - " + str(self.project)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
