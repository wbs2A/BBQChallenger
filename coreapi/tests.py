from django.test import TestCase
from .models import Employee
# Create your tests here.


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='Cleito', drinks=True)
        Employee.objects.create(name='Will', drinks=False)

    def test_title_content(self):
        empl = Employee.objects.get(id=1)
        expected_object_name = f'{empl.name}'
        self.assertEquals(expected_object_name, 'Cleito')

    #TODO
    """
    def test_description_content(self):
        todo = Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')"""