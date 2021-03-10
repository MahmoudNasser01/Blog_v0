from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    image = models.FileField(default='default.svg', upload_to='profile_pics')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'

    #   Change The Image dimensions

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # to make the function run in this class without call it
        img = Image.open(self.image.path)
    
        if img.width > 300 and img.height > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


#   on user created this function will run
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
