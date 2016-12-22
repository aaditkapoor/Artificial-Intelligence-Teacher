from __future__ import unicode_literals

from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username
