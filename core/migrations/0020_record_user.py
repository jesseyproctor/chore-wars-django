# Generated by Django 3.1.7 on 2021-02-21 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210220_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='core.user'),
            preserve_default=False,
        ),
    ]
