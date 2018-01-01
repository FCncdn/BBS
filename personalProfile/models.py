''' The related-with-user field '''
from django.db import models
from bbs.models import UserProfile
# Create your models here.

class FollowShip(models.Model):
    '''follow model'''
    '''follower -> follow'''
    followed = models.ForeignKey(UserProfile, related_name='followed')
    follower = models.ForeignKey(UserProfile, related_name='follower')

    def __str__(self):
        return self.follower.name

class BlackList(models.Model):
    '''black list'''
    '''currentUser blacker'''
    currentUser = models.ForeignKey(UserProfile, related_name='currentUser')
    blacker = models.ForeignKey(UserProfile, related_name='blacker')

    def __str__(self):
        return self.currentUser.name