from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    important = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )