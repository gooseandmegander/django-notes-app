from django.contrib import admin

from notes.models import Note
from notes.models import Tag
from notes.models import Category
from notes.models import PersonalNote

admin.site.register([Note, Tag, Category, PersonalNote])