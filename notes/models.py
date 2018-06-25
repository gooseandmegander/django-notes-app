from django.db import models
from uuid import uuid4

class Note(models.Model):
    # TODO: Add user/author who created it
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    tags = models.TextField(blank = True, default='all')
    categories = models.CharField(max_length = 200, default='all')
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

