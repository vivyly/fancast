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


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('slug', 'name', 'normalized',
                    'image', 'description')


class CharacterSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        model = Character
        fields = ('slug', 'name', 'normalized',
                    'image', 'description', 'project', 'order', 'actors')


