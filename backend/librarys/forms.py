from django.forms import ModelForm
from .models import CommentReaction

class CommentForm(ModelForm):
    class Meta:
        model = CommentReaction
        fields = ('comment',)