from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done_status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content}"
