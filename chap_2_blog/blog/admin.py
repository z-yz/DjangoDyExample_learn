from django.contrib import admin
from .models import Post, Comment

# Register your models here
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','body')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title','author')}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'body')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)