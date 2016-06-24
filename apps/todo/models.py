from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('position', '-created_at')