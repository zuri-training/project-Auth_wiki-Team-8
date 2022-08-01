from django.db import models
from django.utils import timezone

# Create your models here.

class library(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    library_file = models.FileField()
    example_file = models.FileField()
    library_language = models.CharField(max_length=100)
    example_instruction = models.TextField()
    github_link = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return str(self.name) + '['+str(self.author) + ']'
