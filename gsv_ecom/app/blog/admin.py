from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Blog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'parent_id')
    list_filter = ('parent_id',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at', 'is_publish','user')
    list_filter = ('created_at', 'is_publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'content', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
