from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Project(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  project_image = models.ImageField(upload_to = 'projects/', blank=True)
  project_link = models.URLField(max_length=250, blank=True)
  github_link = models.URLField(max_length=250, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  tag = models.ManyToManyField(Tag)


  def __str__(self):
    return self.title





