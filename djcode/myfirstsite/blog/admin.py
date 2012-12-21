from django.contrib import admin
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    list_display = ('title', 'published')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
