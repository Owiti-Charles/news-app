from django.test import TestCase

from .models import Editor, Articles, Tags


class EditorTestClass(TestCase):
    def setUp(self):
        self.charles = Editor(first_name='charles', last_name='mikey', email='info@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles, Editor))

    def test_save_method(self):
        self.charles.save_e()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.charles.delete_e()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)
