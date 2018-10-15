from .models import Comment
from .models import Post
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Comment)
