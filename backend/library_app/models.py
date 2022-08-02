from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# Create your models here.

class LibraryPage(models.Model):
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

class CommentReaction(models.Model):
    comment = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    library = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.like) + '[' +str(self.dislike) + ']'


