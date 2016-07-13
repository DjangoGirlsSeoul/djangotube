from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    episode_number = models.IntegerField()
    video_url = models.URLField()
    video_poster_url = models.URLField()
