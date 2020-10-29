from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    
    portfolioSite = models.URLField(blank=True)

    profilePic = models.ImageField(upload_to='profilePics', blank=True)

    def __str__(self) -> str:
        return self.user.username
