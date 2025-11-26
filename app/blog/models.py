from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Введіть заголовок статті")
    text = models.TextField(help_text="Введіть текст статті")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title