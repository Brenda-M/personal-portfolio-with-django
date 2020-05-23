from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  project_image = models.ImageField(upload_to = 'mainpage/images/', blank=True)
  project_link = models.URLField(max_length=250, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  tag = models.ManyToManyField(Tag)


  def __str__(self):
    return self.title

class Tag (models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


