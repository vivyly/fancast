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
    upvotes = serializers.SerializerMethodField('get_upvotes')
    downvotes = serializers.SerializerMethodField('get_downvotes')
    total = serializers.SerializerMethodField('get_total')

    has_upvoted = serializers.SerializerMethodField('get_has_upvoted')
    has_downvoted = serializers.SerializerMethodField('get_has_downvoted')
    class Meta:
        model = Prospect
        fields = ('slug', 'actor', 'upvotes', 'total', 'downvotes', 'has_upvoted', 'has_downvoted')

    def get_upvotes(self, obj):
        return obj.upvotes

    def get_downvotes(self, obj):
        return obj.downvotes

    def get_has_upvoted(self, obj):
        try:
            request = self.context['request']
            sessionid = request.COOKIES.get('sessionid')
        except KeyError:
            sessionid = ''
        return any(ProspectVote.objects.filter(sessionid=sessionid,
                                                    vote_status=True, prospect=obj))

    def get_has_downvoted(self, obj):
        try:
            request = self.context['request']
            sessionid = request.COOKIES.get('sessionid')
        except KeyError:
            sessionid = ''
        return any(ProspectVote.objects.filter(sessionid=sessionid,
                                                    vote_status=False, prospect=obj))

    def get_total(self, obj):
        return obj.totalvotes


class CharacterSerializer(serializers.ModelSerializer):
    prospects = ProspectSerializer(many=True)
    class Meta:
        model = Character
        fields = ('slug', 'name', 'normalized', 'image',
                    'description', 'project', 'order', 'prospects')


