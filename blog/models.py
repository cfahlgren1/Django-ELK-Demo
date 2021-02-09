from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    pub_date = models.DateField(default=datetime.today)
    author = models.CharField(max_length=255, blank=True, default='')
    is_published = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self):
        return self.title