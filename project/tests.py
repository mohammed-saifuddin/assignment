from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee

class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_employee(self):
        data = {'name': 'John Doe', 'age': 30, 'gender': 'M', 'department': 'IT', 'salary': 5000}
        response = self.client.post('/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().name, 'John Doe')

    def test_list_employees(self):
        Employee.objects.create(name='John Doe', age=30, gender='M', department='IT', salary=5000)
        
