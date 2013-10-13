#/usr/bin/env python
from rest_framework import serializers

from .models import (Project,
                     Character,
                     Actor)

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('slug', 'origin', 'derivation',
                    'origin_title', 'derived_title' )


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('slug', 'name', 'normalized',
                    'image', 'description', 'project', 'order')


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('slug', 'name', 'normalized',
                    'image', 'description')
