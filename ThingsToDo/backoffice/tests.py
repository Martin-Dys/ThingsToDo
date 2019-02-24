
from django.test import TestCase

from .models import Task

class TaskModelTests(TestCase):

    def test_order_was_changed(self):
      
        order_verified = self
        future_order = Task(order=order_verified)
        self.assertIs(future_question.order_was_changed, False)