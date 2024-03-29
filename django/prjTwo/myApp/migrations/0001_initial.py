# Generated by Django 3.2.8 on 2021-10-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('webtoonid', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='webtoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('URL', models.TextField(verbose_name='Site URL')),
                ('thumbnail', models.TextField(verbose_name='Site THUMB')),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
