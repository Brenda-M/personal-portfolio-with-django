from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  technology = models.CharField(max_length=50)
  project_image = models.ImageField(upload_to = 'projects/', blank=True)
  project_link = models.CharField(max_length=500)


  def __str__(self):
    return self.title

