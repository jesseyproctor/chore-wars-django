# Generated by Django 3.1.7 on 2021-02-19 19:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210219_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
