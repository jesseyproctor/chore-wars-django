# Generated by Django 3.1.7 on 2021-02-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20210224_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='comment',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]