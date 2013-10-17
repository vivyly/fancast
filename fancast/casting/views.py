# Create your views here.
from django.views import generic
from rest_framework import (viewsets,
                            generics)

from .models import (Project,
                     Character,
                     Actor,
                     Prospect)
from .serializers import (ProjectSerializer,
                          CharacterSerializer,
                          ActorSerializer)


class ProjectListView(generic.ListView):
    #template_name = "project_list.html"
    template_name = "projects.html"
    def get_queryset(self):
        return Project.objects.all().order_by('published')


class ProjectDetailView(generic.DetailView):
    model = Project
    #template_name = "cast_list.html"
    template_name = "casting.html"
    context_object_name = "slug"


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all().order_by('published')
    serializer_class = ProjectSerializer


class CharacterViewSet(generics.ListCreateAPIView):
    model = Character
    serializer_class = CharacterSerializer

class CharacterDetail(generics.RetrieveAPIView):
    model = Character
    serializer_class = CharacterSerializer
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                return Character.objects.filter(slug=slug)
            except Character.DoesNotExist:
                pass
        return Character.objects.none()

class ActorViewSet(generics.ListAPIView):
    model = Actor
    serializer_class = ActorSerializer
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            character = Character.objects.get(slug=slug)
            eligible_actors = []
            for actor in character.actors:
                try:
                    prospect = Prospect.objects.get(actor = actor,
                                                    character = character)
                    actor.upvotes = prospect.upvotes
                    actor.downvotes = prospect.downvotes
                    actor.total = actor.total
                except Prospect.DoesNotExist:
                    actor.upvotes = 0
                    actor.downvotes = 0
                    actor.total = 0
                eligible_actors.append(actor)
            return eligible_actors
        else:
            return Character.objects.none()


class ActorDetail(generics.RetrieveAPIView):
    serializer_class = ActorSerializer
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                return Actor.objects.filter(slug=slug)
            except Actor.DoesNotExist:
                pass
        return Actor.objects.none()
