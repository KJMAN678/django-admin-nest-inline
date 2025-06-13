from django.db import models


class Blog(models.Model):
    content = models.TextField(verbose_name="スポット名")

    def __str__(self):
        return f"{self.content[:50]}"

    class Meta:
        verbose_name = "スポット"
        verbose_name_plural = "スポット"


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="スポット名",
    )
    content = models.TextField(verbose_name="親ブロック名")

    def __str__(self):
        return f"{self.content[:50]}"

    class Meta:
        verbose_name = "親ブロック"
        verbose_name_plural = "親ブロック"


class ReplyComment(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name="親ブロック名",
    )
    content = models.TextField(verbose_name="子ブロック名")

    def __str__(self):
        return f"Reply {self.id} to Comment {self.comment.id}: {self.content[:50]}..."

    class Meta:
        verbose_name = "子ブロック"
        verbose_name_plural = "子ブロック"
