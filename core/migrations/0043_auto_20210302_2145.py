# Generated by Django 3.1.7 on 2021-03-02 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20210302_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pod',
            name='teams',
        ),
        migrations.AddField(
            model_name='pod',
            name='pod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feed', to='core.pod'),
            preserve_default=False,
        ),
    ]
