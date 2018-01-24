# Generated by Django 2.0 on 2018-01-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]