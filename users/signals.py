from users.models import Profile
from freelancer import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def CreateProfile(sender, instance, created, *args, **kwargs):
    if created:
        user_obj = instance
        profile = Profile.objects.create(
            user=user_obj,
            bio=user_obj.about
        )





# def profileDeleted(sender, instance, *args, **kwargs):
#     print('deleting profile...')
# post_save.connect(CreateProfile, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile)