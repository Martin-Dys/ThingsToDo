
from django.urls import path
from .views import ListTaskView, TaskDetailView

app_name = 'backoffice'

urlpatterns = [
    # ex: /backoffice/
    #path('', views.index, name='index'),
    # ex: /backoffice/5/
    #path('<int:task_id>/', views.detail, name='detail'),
    # ex: /backoffice/5/results/
    #path('<int:task_id>/results/', views.results, name='results'),
    # ex: /backoffice/5/subtask/
    #path('<int:task_id>/subtask/', views.subtask, name='subtask'),
    path('task/', ListTaskView.as_view(), name="task-all"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
]



