from django.contrib import admin
from django.utils.html import format_html
from .models import Blog, Comment, ReplyComment


class ReplyCommentInline(admin.TabularInline):
    model = ReplyComment
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "get_comment_link", "get_comments"]
    list_display_links = ["content"]
    inlines = [CommentInline]

    def get_comment_link(self, obj):
        url = f"/admin/blog/comment/add/?blog={obj.id}"
        return format_html('<a href="{}">親ブロックを追加</a>', url)

    get_comment_link.short_description = "親ブロックを追加"

    def get_comments(self, obj):
        comments = obj.comments.all()
        if not comments:
            return "コメントなし"

        links = []
        for comment in comments:
            url = f"/admin/blog/comment/{comment.id}/change/"
            links.append(f'<a href="{url}">親ブロック{comment.id}</a>')
        return format_html(", ".join(links))

    get_comments.short_description = "親ブロック一覧"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "blog", "content"]
    list_display_links = ["content"]
    inlines = [ReplyCommentInline]


@admin.register(ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "comment", "content"]
    list_display_links = ["content"]
