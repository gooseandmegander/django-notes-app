from django.contrib import admin

from bookmarks.models import BookMark
from bookmarks.models import BookMark_Folder
from bookmarks.models import PersonalBookMark

admin.site.register((BookMark, BookMark_Folder, PersonalBookMark))