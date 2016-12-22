from __future__ import unicode_literals

from django.db import models


class MarketPlace(models.Model):
	by = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)
	date_uploaded = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	packId = models.CharField(max_length=20)
	
	def __unicode__(self):
		return "Question on  "  + self.subject


