from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class FriUser(AbstractUser):
      signature = models.CharField(default='this guy is lazy to leave something'                  ,max_length=256)
      def __unicode__(self):
           return self.username

class Affair(models.Model):
      author = models.ForeignKey('FriUser')
      content = models.TextField()
      pub_date = models.DateTimeField(auto_now_add=True,editable=True)
      like_count = models.IntegerField()
      
      def __unicode__(self):
           return self.content

class Comment(models.Model):
      affair = models.ForeignKey('Affair')
      content = models.TextField()
      pub_date = models.DateTimeField(auto_now_add=True,editable=True)
      author = models.ForeignKey('FriUser')

      

