# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Playera

# Register your models here.
@admin.register(Playera)
class AdminUmbrella(admin.ModelAdmin):
	list_display = ('id', 'name', 'ip', 'state')
	list_filter = ('state',)


# @admin.register(Zone)
# class AdminUmbrella(admin.ModelAdmin):
# 	list_display = ('id', 'Name', 'Description'#, 'Zone'
#     )
# 	list_filter = ('State',)
