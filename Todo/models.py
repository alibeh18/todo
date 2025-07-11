from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=10000)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task