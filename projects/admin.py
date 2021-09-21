from __future__ import unicode_literals

from django.contrib import admin
from .models import Project,Profile
# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)