# Generated by Django 4.1.6 on 2023-02-03 23:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='article',
            field=models.TextField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]