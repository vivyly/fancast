# Create your views here.
from django.views import generic
from rest_framework import (viewsets,
                            generics)

from .models import (Project,
                     Character,
                     Actor)
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
    serializer_class = ActorSerializer
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            character = Character.objects.get(slug=slug)
            return character.actors
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
