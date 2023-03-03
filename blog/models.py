from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    article = RichTextField()
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs_images/')
    slug = models.SlugField(null=True, blank=True, max_length=150)
    read_time = models.IntegerField()
    popular = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=25, default='some string')

    def __str__(self):
        return self.name
