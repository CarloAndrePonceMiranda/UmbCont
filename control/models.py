# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import GenericIPAddressField


# Create your models here.

class Playera(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(null=False, blank=False, max_length=255)
    state = models.BooleanField(null=False, blank=False, max_length=255)
    #Zone = models.ForeignKey('Zone', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# class Zone(models.Model):
# 	Name = models.CharField(max_length=255)
#   Description = models.CharField(max_length=255)
#
# 	def __str__(self):
# 		return self.Name
