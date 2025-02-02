from django.db import models
from startups.models import Tag, Startup
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
            max_length=63,
            help_text='A label for URL Config',
            unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
            'date published',
            auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(
                self.title,
                self.pub_date.strftime('%Y-%m-%d'))
