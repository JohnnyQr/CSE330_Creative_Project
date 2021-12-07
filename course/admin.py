from django.contrib import admin
from .models import Course, Comment
# Register your models here.


class CourseManager (admin.ModelAdmin):
    list_display = ['title', 'instrument', 'price', 'level', 'location', 'certification']
    list_filter = ['instrument', 'level', 'location']
    search_fields = ['title', 'instrument']


class CommentManager (admin.ModelAdmin):
    list_display = ['content']


admin.site.register(Course, CourseManager)
admin.site.register(Comment, CommentManager)
