from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(
        max_length=200, 
        blank=True,
        null=True,)
    priority = models.IntegerField(default=0)
    start_date = models.DateTimeField('start_date')
    end_date = models.DateTimeField('end_date')
    place = models.CharField(
        max_length=200, 
        blank=True,
        null=True,)
    def __str__(self):
        return "{} - {}".format(self.name, self.priority)

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,)
    order = models.IntegerField(default=1)
    def __str__(self):
        return "{} - {}".format(self.name, self.order)