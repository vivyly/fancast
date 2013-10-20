import simplejson

from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import (csrf_exempt,
                                         requires_csrf_token)
from rest_framework import (viewsets,
                            generics,
                            )

from rest_framework.renderers import JSONRenderer

from .models import (Project,
                     Character,
                     Actor,
                     Prospect,
                     ProspectVote)

from .serializers import (ProjectSerializer,
                          CharacterSerializer,
                          ProspectSerializer,
                          ActorSerializer)

from .forms import (AddActor,
                    AddCharacter)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



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
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['sessionID'] = self.request.COOKIES.get('sessionid')
        return context


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


@csrf_exempt
@requires_csrf_token
def vote(request, slug):
    if request.method == "POST" or request.method == "PUT":
        #this is probably not the right way to do it, need
        #to figure out why post params are coming in as a string
        #instead of a QueryDict
        params = simplejson.loads(request.body)
        vote_status = params.get('vote_status', 0)
        prospect = Prospect.objects.get(slug=slug)
        sessionid = request.session.session_key
        try:
            prospect_vote = ProspectVote.objects.get(prospect=prospect,
                                    sessionid=sessionid)
        except ProspectVote.DoesNotExist:
            prospect_vote = ProspectVote()
            prospect_vote.sessionid = sessionid
            prospect_vote.prospect = prospect
        prospect_vote.vote_status = int(vote_status)
        prospect_vote.save()
    prospects = Prospect.objects.filter(character=prospect.character)
    serializer = ProspectSerializer(prospects, many=True,
                                        context = {'request':request})
    serializer.is_valid()
    return JSONResponse(serializer.data)


@csrf_exempt
@requires_csrf_token
def add_actor(request):
    if request.method == "POST":
        #this is probably not the right way to do it, need
        #to figure out why post params are coming in as a string
        #instead of a QueryrDict
        params = simplejson.loads(request.body)
        form = AddActor(params)
        if form.is_valid():
            _actor = form.save(request)
            character = Character.objects.get(slug=params.get('character_id'))
            prospects = Prospect.objects.filter(character=character)
            serializer = ProspectSerializer(prospects, many=True,
                                        context = {'request':request})
            serializer.is_valid()
            return JSONResponse(serializer.data)
        else:
            errors = [(k, v[0].__unicode__()) for k, v in
                                                form.errors.items()]
            return JSONResponse({'errors':errors})
    return JSONResponse({})

@csrf_exempt
@requires_csrf_token
def add_character(request):
    if request.method == "POST":
        #this is probably not the right way to do it, need
        #to figure out why post params are coming in as a string
        #instead of a QueryrDict
        print request
        params = simplejson.loads(request.body)
        print params
        form = AddCharacter(params)
        if form.is_valid():
            character = form.save()
            serializer = CharacterSerializer([character], many=True,
                                    context = {'request':request})
            serializer.is_valid()
            return JSONResponse(serializer.data)
        else:
            errors = [(k, v[0].__unicode__()) for k, v in
                                                form.errors.items()]
            return JSONResponse({'errors':errors})
    return JSONResponse({})
