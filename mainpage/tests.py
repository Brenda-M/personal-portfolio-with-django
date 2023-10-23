from django.test import TestCase
from .models import  Project

class ProjectTestClass(TestCase):

  def setUp(self):
    self.project = Project(title="test app", description='an app to test the functionality of the project')

  def test_instance(self):
    self.assertTrue(isinstance(self.project, Project))
  
  def test_save_projects(self):
    self.project.save_projects()
    projects = Project.objects.all()
    self.assertTrue(len(projects) > 0)
  
  def tearDown(self):
    self.project.save_projects()
    Project.objects.all().delete()