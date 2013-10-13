#/usr/bin/env python
from django.contrib import admin
from .models import Project, Character, Actor, Prospect

admin.site.register(Project)
admin.site.register(Character)
admin.site.register(Actor)
admin.site.register(Prospect)

