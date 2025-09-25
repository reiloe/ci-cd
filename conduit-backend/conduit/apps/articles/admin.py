from django.contrib import admin

from .models import Tag, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag", "slug"]
    search_fields = ["tag"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author"]
    search_fields = ["title", "slug"]
    list_filter = ["author"]