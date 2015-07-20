#-*- coding: utf-8 -*-
from django.db import models

class UserLanguage(models.Model):
    user = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.user
