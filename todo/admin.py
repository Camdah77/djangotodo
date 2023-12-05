from __future__ import unicode_literals
from django.contrib import admin
from .models import Item

#register the model
admin.site.register(Item)
