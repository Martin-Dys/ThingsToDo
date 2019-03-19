from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Task, Subtask
 

from rest_framework import generics
from .serializers import TaskSerializer

class ListTaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_task = Task.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            priority=request.data["priority"],
            start_date=request.data["start_date"],
            end_date=request.data["end_date"],
        )
        return Response(
            data=TaskSerializer(a_task).data,
            status=status.HTTP_201_CREATED
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            return Response(TaskSerializer(a_task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            serializer = TaskSerializer()
            updated_task = serializer.update(a_task, request.data)
            return Response(TaskSerializer(updated_task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_task = self.queryset.get(pk=kwargs["pk"])
            a_task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )





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