from django.contrib import admin
from .models import CommentReaction, LibraryPage, Reactions

# Register your models here.


admin.site.register(LibraryPage)
admin.site.register(CommentReaction)
admin.site.register(Reactions)
