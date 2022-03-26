from django.test import TestCase
from .models import Task
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
# Create your tests here.

class TaskCreate(TestCase):
    def test_TaskCreate(self):
        data={
            'Title':'testing',
            'description':'fghdfghfd',
            'complete':'',
        
        }


