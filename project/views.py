from django.http import Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from project.models import Project
from project.serializers import ProjectSerializer


def list_projects(request):
    projects = Project.objects.filter(team__in=request.user.teams.all())
    serializer = ProjectSerializer(projects, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

def get_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404("Project not found")
    serializer = ProjectSerializer(project, context={'request': request})
    data = serializer.data
    data['timelogs'] = request.build_absolute_uri('timelogs/')
    return JsonResponse(data, safe=False)
