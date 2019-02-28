from .models import Task, Subtask
"""
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    latest_task_list = Task.objects.order_by('-start_date')[:10]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'backoffice/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'backoffice/detail.html', {'task': task})

def results(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'backoffice/results.html', {'task': task})

def subtask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    try:
        selected_subtask = task.subtask_set.get(pk=request.POST['subtask'])
    except (KeyError, Subtask.DoesNotExist):
        # Redisplay the task voting form.
        return render(request, 'backoffice/detail.html', {
            'subtask': subtask,
            'error_message': "You didn't select a subtask.",
        })
    else:
        selected_subtask.order += 1          
        selected_subtask.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('backoffice:results', args=(task.id,)))
"""

from rest_framework import generics
from .serializers import TaskSerializer

class ListTaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
