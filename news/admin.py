from django.contrib import admin

from .models import Articles, Tags, Editor

admin.site.register(Editor)
admin.site.register(Articles)
admin.site.register(Tags)
