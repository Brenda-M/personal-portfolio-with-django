from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  technology = models.CharField(max_length=50)

  def __str__(self):
    return self.title