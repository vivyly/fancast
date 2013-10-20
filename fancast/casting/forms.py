#/usr/bin/env python
from django import forms

from .models import (Character,
                     Actor,
                     Prospect,
                     ProspectVote)
from fancast.lib.name import normalize

class AddActor(forms.Form):
    name = forms.CharField(required=True)
    image = forms.URLField(required=True)
    character_id = forms.CharField(required=True)


    def clean(self):
        data = self.cleaned_data
        character_id = data.get('character_id')
        try:
            character = Character.objects.get(slug=character_id)
            data['character'] = character
        except Character.DoesNotExist:
            raise forms.ValidationError("This character does not exist")

        return data

    def save(self, request):
        sessionid = request.COOKIES.get('sessionid')
        data = self.cleaned_data
        character = data.get('character')
        try:
            name = data.get('name')
            actor = Actor.objects.get(normalized=normalize(name))
        except Actor.DoesNotExist:
            actor = Actor()
            actor.name = name
            actor.normalized = normalize(name)
            actor.image = data.get('image')
            actor.save()
        try:
            prospect = Prospect.objects.get(actor=actor,
                                            character=character)
        except Prospect.DoesNotExist:
            prospect = Prospect()
            prospect.actor = actor
            prospect.character = character
            prospect.save()
        try:
            vote = ProspectVote.objects.get(prospect=prospect,
                                            sessionid = sessionid)
        except ProspectVote.DoesNotExist:
            vote = ProspectVote()
            vote.prospect = prospect
            vote.sessionid = sessionid
            vote.vote_status = True
            vote.save()
        return character

