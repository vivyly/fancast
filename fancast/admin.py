#/usr/bin/env python
from django.contrib import admin
from fancast.casting.models import Project, Character, Actor

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("derived_title")


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    fields = ['name', 'normalized', 'image', 'description', 'project', 'order']


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    fields = ['name', 'normalized', 'image', 'description']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Actor, ActorAdmin)
