from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(
            max_length=31, unique=True)
    slug = models.SlugField(
            max_length=31,
            unique=True,
            help_text='A label for URL config.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Startup(models.Model):
    name = models.CharField(
            max_length=31,
            db_index=True
            )
    slug = models.SlugField(
            max_length=31,
            unique=True,
            help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField(
            'date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)

    class Meta:
        verbose_name = 'blog_post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

