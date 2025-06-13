from django.db import models


class Blog(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return f"Blog {self.id}: {self.content[:50]}..."


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    
    def __str__(self):
        return f"Comment {self.id} on Blog {self.blog.id}: {self.content[:50]}..."


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    
    def __str__(self):
        return f"Reply {self.id} to Comment {self.comment.id}: {self.content[:50]}..."
