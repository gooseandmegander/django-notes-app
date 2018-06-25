from django.db import models
from uuid import uuid4

class BookMark(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    bookmark_name = models.CharField(max_length = 200)
    bookmark_folder = models.CharField(max_length = 200)
    hyperlink = models.URLField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)


