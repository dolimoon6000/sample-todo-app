from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('position', '-created_at')