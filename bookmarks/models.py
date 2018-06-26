from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

class BookMark_Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    folder_name = models.CharField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class BookMark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    bookmark_name = models.CharField(max_length=200)
    bookmark_folder = models.ForeignKey(BookMark_Folder, null=True, blank=True, on_delete=models.SET_NULL)
    hyperlink = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalBookMark(BookMark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)