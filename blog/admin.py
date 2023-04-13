from django.contrib import admin

from .models import Post

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'desc', 'created', 'updated')
    list_filter = ('title', 'desc', 'created', 'updated')
    search_fields = ('title', 'desc')
    list_display_links = ('id', 'title')

    readonly_fields = ('created', 'updated')

