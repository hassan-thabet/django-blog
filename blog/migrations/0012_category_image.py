# Generated by Django 4.1.6 on 2023-03-06 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_published_at_blog_updated_at_blog_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category_images/'),
            preserve_default=False,
        ),
    ]
