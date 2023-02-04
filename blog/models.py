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
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25, default='some string')

    def __str__(self):
        return self.name
