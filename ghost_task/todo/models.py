from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, default=None)
    status = models.ForeignKey("todo.Status", on_delete=models.CASCADE)
    text = models.TextField()
    spent = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

class Status(models.Model):
    status = models.CharField(max_length=50, blank=True, null=True, default=None, unique=True)    

    def __str__(self):
        return self.status