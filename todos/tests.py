from django.test import TestCase
from django.urls import reverse
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "learn",
            body = "it's important to learn"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "learn")
        self.assertEqual(self.todo.body, "it's important to learn")
        self.assertEqual(str(self.todo), "learn")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code,200)
        self.assertEqual(Todo.objects.count(),1)
        self.assertContains(response,self.todo)

    def test_api_detailview(self):
        response = self.client.get(reverse("todo_detail",kwargs={"pk":self.todo.id}),format="json")
        self.assertEqual(response.status_code,200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "learn")

