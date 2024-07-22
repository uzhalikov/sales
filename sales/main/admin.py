from django.contrib import admin
from .models import *

admin.site.register(User)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'price', 'author', 'created']
    fields = ['title', 'description', 'price', 'author']