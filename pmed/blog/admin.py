# coding: utf-8
from django.contrib import admin
from blog.models import Post # модель из blog/models.py

admin.site.register(Post)
