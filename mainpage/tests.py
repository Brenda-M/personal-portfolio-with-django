from django.test import TestCase
from .models import Tag, Project

# class ProjectTestClass(TestCase):
#   def setUp(self):
#     self.app = Project(title='tech app', description='test application', project_image='',)


# title = models.CharField(max_length=50)
#   description = models.CharField(max_length=250)
#   project_image = models.ImageField(upload_to = 'mainpage/images/', blank=True)
#   project_link = models.URLField(max_length=250, blank=True)
#   pub_date = models.DateTimeField(auto_now_add=True)
#   tag = models.ManyToManyField(Tag