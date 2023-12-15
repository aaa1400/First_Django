from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'login_require', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    # ordering = ['-created_date']
    search_fields = ['content', 'title']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approach', 'created_date')
    list_filter = ('post', 'approach')
    search_fields = ['name', 'post']


# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
