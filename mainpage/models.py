from django.db import models

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)  # Use AutoField for primary key
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Project(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  project_image = models.ImageField(upload_to = 'projects/', blank=True)
  project_link = models.URLField(max_length=250, blank=True)
  github_link = models.URLField(max_length=250, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  tag = models.ManyToManyField(Tag)

  def save_projects(self):
    self.save()


  def __str__(self):
    return self.title





