#/usr/bin/env python
from django import forms

from .models import (Project,
                     Character,
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

        try:
            name = data.get('name')
            actor = Actor.objects.get(normalized=normalize(name))
            try:
                Prospect.objects.get(actor = actor,
                                               character = character)
                raise forms.ValidationError(
                    "This actor already exists for this character")
            except Prospect.DoesNotExist:
                pass
        except Actor.DoesNotExist:
            pass
        return data

    def save(self):
        data = self.cleaned_data
        character = data.get('character')
        name = data.get('name')
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
        return actor


class AddCharacter(forms.Form):
    name = forms.CharField(required=True)
    image = forms.URLField(required=True)
    project_id = forms.CharField(required=True)

    def clean(self):
        data = self.cleaned_data
        project_id = data.get('project_id')
        name = data.get('name')
        if project_id:
            try:
                project = Project.objects.get(slug=project_id)
                data['project'] = project
                try:
                    Character.objects.get(project=project,
                                            normalized=normalize(name))
                    raise forms.ValidationError(
                            "Character already exists in this project.")
                except Character.DoesNotExist:
                    pass
            except Project.DoesNotExist:
                raise forms.ValidationError("Project does not exist.")
        else:
            raise forms.ValidationError("project required")
        return data

    def calculate_order(self, project):
        return Character.objects.filter(project=project).count()

    def save(self):
        data = self.cleaned_data
        project = data.get('project')
        character = Character()
        character.name = data.get('name')
        character.normalized = normalize(character.name)
        character.image = data.get('image')
        character.project = project
        character.order = self.calculate_order(project)
        character.save()
        return character


