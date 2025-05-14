from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    skill = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to="static/img/")
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - ({self.year})"


class Experience(models.Model):
    name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    skill = models.ManyToManyField(Skill)