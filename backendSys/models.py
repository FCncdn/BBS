from django.db import models
from bbs.models import UserProfile
from datetime import date
# Create your models here.
class Choices(models.Model):
    '''mulit choice option'''
    description  = models.CharField(max_length=300)
    def __str__(self):
        return self.description

class Administrator(models.Model):
    '''admin model'''
    '''different with superuser'''
    admin = models.ForeignKey(
        UserProfile,
         related_name='admin',
         on_delete=models.CASCADE,
        )
    block = models.ManyToManyField(Choices, related_name='block')
    permission = models.ManyToManyField(Choices, related_name='permission')
    time = models.DateField(auto_now_add=True)
    def __str__(self):            
            return self.admin.user.username
    class Meta:
        permissions = (
            ('move_post','Move the post'),
            ('delete_post', 'Delete the post'),
            ('ban_post', 'Banned specified user to post'),
            ('ban_user', 'Banned specified user to visit'),
        )