from django.contrib import admin

from bookmarks.models import BookMark
from bookmarks.models import BookMark_Folder
from bookmarks.models import PersonalBookMark

# register models to production ready administrative interface
# localhost:8000
# as-fast-as-possible backend interface [ https://docs.djangoproject.com/en/2.0/ref/contrib/admin/ ]
admin.site.register((BookMark, BookMark_Folder, PersonalBookMark))