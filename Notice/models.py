from django.db import models


class Notice(models.Model):
    id: int
    title = models.CharField(max_length=100)
    desc = models.TextField()
