from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Task, Subtask


def index(request):
    latest_task_list = Task.objects.order_by('-start_date')[:10]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'backoffice/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'backoffice/detail.html', {'task': task})

def results(request, task_id):
    response = "You're looking at the results of task %s."
    return HttpResponse(response % task_id)

def subtask(request, task_id):
    return HttpResponse("You're voting on task %s." % task_id)