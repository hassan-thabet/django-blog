# Generated by Django 4.1.6 on 2023-02-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='blogs/'),
            preserve_default=False,
        ),
    ]
