# Generated by Django 2.0.6 on 2018-06-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20180625_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
