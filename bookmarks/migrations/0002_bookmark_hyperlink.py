# Generated by Django 2.0.6 on 2018-06-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='hyperlink',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
    ]
