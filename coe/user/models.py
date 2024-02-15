from django.contrib.auth.models import User
from django.db import models
#from character.models import character

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #character = models.ForeignKey(character, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

