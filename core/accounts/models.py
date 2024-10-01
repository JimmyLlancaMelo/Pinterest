from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save

# Cuando creamos un usuario se pondra por automatico las siguientes imagenes

def user_directory_path_profile(instance, filenmae):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    fullpath =os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(fullpath):
        os.remove(fullpath)
    
    return profile_picture_name

def user_directory_path_banner(instance, filenmae):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    fullpath =os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(fullpath):
        os.remove(fullpath)
    
    return profile_picture_name



VERIFICATION_OPTIONS=(
    ('unverified','unverified'),
    ('verified','verified'),
    
)

class User(AbstractUser):
    
    stripe_customer_id = models.CharField(max_length=50)


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/UserDefaultProfile.png',upload_to=user_directory_path_profile)
    banner = models.ImageField(default='users/UserDefaultBg.jpg',upload_to=user_directory_path_banner)
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')
    coins = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=True)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=150, null=True, blank=True)
    
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    
    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)