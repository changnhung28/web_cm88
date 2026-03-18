from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title