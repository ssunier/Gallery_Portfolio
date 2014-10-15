import datetime

from django.db import models
from django.utils import timezone


#art portfolio
class Collection(models.Model):
  collection_id = models.AutoField(primary_key=True)
  collection = models.CharField(max_length=200)

  def __str__(self):
    return self.collection

class Gallery(models.Model):
  def _collections(self):
    return [(c.col_id, c.collection) for c in Collection.objects.all()]

  art_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  collection = models.ForeignKey(Collection)
  link = models.URLField(max_length=255)
  post_desc = models.CharField(max_length=500, null=True, blank=True)
  post_date = models.DateTimeField(default=timezone.now)

  objects = models.Manager()

  def __str__(self):
    return self.title

#music portfolio
class Music(models.Model):
  SONG = 'S'
  VIDEO = 'V'
  POST_TYPE_CHOICES = (
    (SONG, 'Song'),
    (VIDEO, 'Video'),
    )
  music_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  album = models.CharField(max_length=200)
  post_type = models.CharField(max_length=1,
                               choices=POST_TYPE_CHOICES,
                               default=SONG)
  link = models.URLField(max_length=255)
  post_desc = models.CharField(max_length=500, null=True, blank=True)
  post_date = models.DateTimeField(default=timezone.now)

  objects = models.Manager()

  def __str__(self):
    return self.title + ', ' + self.post_type
