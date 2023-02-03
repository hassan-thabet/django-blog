from django.db import models

# image
# title
# article
# author
# tags
# category
# published at


class Blog(models.Model):
    author = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    article = models.TextField(max_length=5000)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
