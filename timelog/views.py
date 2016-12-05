from django.http import Http404, JsonResponse
from timelog.models import TimeLog
from timelog.serializers import TimeLogSerializer


def list_timelogs(request, project_pk=None, user_pk=None):
    filters = {}
    if 'started_at' in request.GET:
        filters['started_at__gte'] = request.GET['started_at']
    if user_pk:
        filters['user__pk'] = user_pk
    if project_pk:
        filters['project__pk'] = project_pk
    if not filters:
        raise Http404("Please, provide project or user for log list.")
    timelogs = TimeLog.objects.filter(**filters)
    serializer = TimeLogSerializer(timelogs, many=True, context={'request': request})
    # prepare user base totals:
    data = {'total': 0}
    for log in timelogs:
        username = log.user.username
        if username in data.keys():
            data[username] += log.duration
        else:
            data[username] = log.duration
        data['total'] += log.duration
    data['items'] = serializer.data
    return JsonResponse(data, safe=False)

def get_timelog(request, pk, project_pk=None, user_pk=None):
    try:
        if user_pk:
            timelog = TimeLog.objects.get(pk=pk, user__pk=user_pk)
        elif project_pk:
            timelog = TimeLog.objects.get(pk=pk, project__pk=project_pk)
        else:
            raise Http404("Please, provide project or user for log.")
    except TimeLog.DoesNotExist:
        raise Http404
    serializer = TimeLogSerializer(timelog, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

def create_timelog(request):
    pass

def update_timelog(request, pk):
    pass

def delete_timelog(request, pk):
    pass
