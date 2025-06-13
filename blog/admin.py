from django.contrib import admin
from .models import Blog, Comment, ReplyComment


class ReplyCommentInline(admin.TabularInline):
    model = ReplyComment
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'content']
    list_filter = ['blog']
    inlines = [ReplyCommentInline]


@admin.register(ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'content']
    list_filter = ['comment__blog']
