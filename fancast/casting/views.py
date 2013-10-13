# Create your views here.
from django.views import generic

from .models import Project


class ProjectListView(generic.ListView):
    template_name = "project_list.html"
    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = "cast_list.html"
    context_object_name = "slug"

