from django.db import models

# Create your models here.
class Yt_Video(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    thumbnail = models.URLField()
    length = models.IntegerField()
    views = models.IntegerField()
    
    def __str__(self):
        return f"{self.author} | {self.title}"