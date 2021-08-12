from django.db import models
from freelancer import settings
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-pics/', default='profile-pics/user-default.png', blank=True, null=True)
    social_github = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)