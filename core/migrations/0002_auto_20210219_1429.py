# Generated by Django 3.1.6 on 2021-02-19 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('detail', models.TextField(max_length=1000)),
                ('chore_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slogan', models.TextField(max_length=1000)),
                ('theme_song', models.CharField(blank=True, max_length=500, null=True)),
                ('background_image', models.CharField(max_length=500, null=True)),
                ('dashboard_style', models.CharField(max_length=100)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='kids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField(max_length=1000)),
                ('chore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chore')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reverse', to='core.chore', to_field='chore_type')),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('teams', models.ManyToManyField(related_name='teams', to='core.Team')),
            ],
        ),
        migrations.AddField(
            model_name='chore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
