# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from rest_framework import routers

from .casting.views import (ProjectListView,
                    ProjectDetailView,
                    ProjectViewSet,
                    CharacterViewSet,
                    CharacterDetail,
                    ActorViewSet,
                    ActorDetail)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

SLUG = '''[a-zA-Z0-9_\-]+'''

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/character/(?P<slug>%s)$' % SLUG,
                CharacterDetail.as_view(), name="character-detail" ),
    url(r'^api/characters/(?P<slug>%s)$' % SLUG,
                CharacterViewSet.as_view(), name="character-list" ),
    url(r'^api/actor/(?P<slug>%s)$' % SLUG,
                ActorDetail.as_view(), name="actor-detail" ),
    url(r'^api/actors/(?P<slug>%s)$' % SLUG,
                ActorViewSet.as_view(), name="actor-list" ),
    url(r'^api/vote/(?P<slug>%s)$' % SLUG, "fancast.casting.views.vote"),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include("rest_framework.urls",
                                        namespace="rest_framework")),
    url(r'^casting/(?P<slug>%s)$' % SLUG,
                ProjectDetailView.as_view(), name="project-detail"),
    url(r'^', ProjectListView.as_view(), name="project-list"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
