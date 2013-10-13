from operator import itemgetter

from django.db import models

from shortuuidfield import ShortUUIDField

MEDIUM_CHOICES = [(x, x) for x in ['movie',
                                  'tv',
                                  'book',
                                  'comicbook',
                                  'play',
                                  'theatre',
                                  'shortfilm',
                                  'shortstory',
                                  'cartoon',
                                  'anime',
                                  'manga',
                                  'videogame'
                                  'documentary',
                                  'life'
                                  ]]

class BaseModel(models.Model):
    slug = ShortUUIDField(unique=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Project(BaseModel):
    origin = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
    derivation = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
    origin_title = models.CharField(max_length=255, blank=False)
    derived_title = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return u"<Project: %s >" % self.derived_title

    @property
    def characters(self):
        return Character.objects.filter(project = self).order_by('order')

class Character(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    normalized = models.CharField(max_length=255, blank=False)
    image = models.URLField(blank=True)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, null=True, blank=False)
    order = models.IntegerField()

    def __unicode__(self):
        return u"<Character: %s >" % self.name

    @property
    def actors(self):
        return Actor.objects.filter(prospect__character = self)

    @property
    def actors_ordered(self):
        prospects = Prospect.objects.filter(character=self)
        actors = []
        for prospect in prospects:
            actors.append([prospect.totalvotes, prospect.actor])
        sorted_actors = [actor for actor in sorted(actors, key=itemgetter(0))]
        sorted_actors.reverse()
        return sorted_actors


class Actor(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    normalized = models.CharField(max_length=255, blank=False)
    image = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u"<Actor: %s >" % self.name

class Prospect(BaseModel):
    character = models.ForeignKey(Character)
    actor = models.ForeignKey(Actor)

    @property
    def upvotes(self):
        return ProspectVote.objects.filter(
                prospect=self, vote_status=True).count()

    @property
    def downvotes(self):
        return ProspectVote.objects.filter(
                prospect=self, vote_status=False).count()

    @property
    def totalvotes(self):
        return self.upvotes - self.downvotes


class ProspectVote(models.Model):
    sessionid = models.CharField(max_length=255)
    prospect = models.ForeignKey(Prospect)
    vote_status = models.BooleanField()

