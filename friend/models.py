from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class FriUser(AbstractUser):
      signature = models.CharField(default='this guy is lazy to leave something'                  ,max_length=256)
      def __unicode__(self):
           return self.username


