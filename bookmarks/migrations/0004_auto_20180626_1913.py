# Generated by Django 2.0.6 on 2018-06-26 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20180625_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='bookmark_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookmarks.BookMark_Folder'),
        ),
    ]
