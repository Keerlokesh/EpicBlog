# Generated by Django 3.1.1 on 2020-09-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EpicBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='EpicBlog/images'),
        ),
    ]
