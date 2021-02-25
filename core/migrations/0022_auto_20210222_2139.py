# Generated by Django 3.1.7 on 2021-02-22 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210222_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='slogan',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]