from django.db import models


class Project(models.Model):
    """
    Projects
    """

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    type = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
