from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class FriUser(AbstractUser):
      signature = models.CharField(default='this guy is lazy to leave something'                  ,max_length=256)
      friends_id = models.CharField(null=True,max_length=256)
      add_fri_id = models.CharField(null=True,blank=True,max_length=256)
      email_address = models.CharField(max_length=256)
      phone = models.CharField(null=True,blank=True,max_length=256)

      def __unicode__(self):
           return self.username

class Affair(models.Model):
      author = models.ForeignKey('FriUser')
      content = models.TextField()
      pub_date = models.DateTimeField(auto_now_add=True,editable=True)
      like_count = models.IntegerField(default=0)
      
      def __unicode__(self):
           return self.content

class Comment(models.Model):
      affair = models.ForeignKey('Affair')
      content = models.TextField()
      pub_date = models.DateTimeField(auto_now_add=True,editable=True)
      author = models.ForeignKey('FriUser')

     
class Upload(models.Model):
      user = models.OneToOneField(FriUser) 
      image  = models.ImageField( upload_to='friend/media/',default='friend/media/no_img.jpg')
