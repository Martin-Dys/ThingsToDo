
from django.urls import path
from .views import ListTaskView, TaskDetailView

app_name = 'backoffice'

urlpatterns = [
    path('task/', ListTaskView.as_view(), name="task-all"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
]



