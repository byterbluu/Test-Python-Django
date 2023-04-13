from django.contrib import admin

#models
from .models import Project

# Register your models here.

# admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created', 'updated')
    list_filter = ('title', 'desc', 'created', 'updated')
    search_fields = ('title', 'desc')
    list_display_links = ('id', 'title')

