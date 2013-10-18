#/usr/bin/env python
from rest_framework import serializers

from .models import (Project,
                     Character,
                     Prospect,
                     ProspectVote,
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


class ProspectVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectVote
        fields = ('sessionid', 'vote_status')


class ProspectSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    votes = serializers.RelatedField(many=True)
    class Meta:
        model = Prospect
        fields = ('slug', 'actor', 'votes',)

class CharacterSerializer(serializers.ModelSerializer):
    prospects = ProspectSerializer(many=True)
    class Meta:
        model = Character
        fields = ('slug', 'name', 'normalized', 'image',
                    'description', 'project', 'order', 'prospects')


