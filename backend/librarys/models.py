from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

class LibraryPage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    library_file = models.FileField(upload_to='libraries')
    example_file = models.FileField(upload_to='examples')
    library_version = models.CharField(max_length=50)
    library_language = models.CharField(max_length=100)
    example_instruction = models.TextField()
    github_link = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + '['+str(self.author) + ']'


class CommentReaction(models.Model):
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like = models.IntegerField()
    dislike = models.IntegerField()
    library = models.ForeignKey(
        LibraryPage, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.like) + '[' + str(self.dislike) + ']'
