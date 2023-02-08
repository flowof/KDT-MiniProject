# Generated by Django 3.2.8 on 2021-10-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='webtoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('URL', models.URLField(verbose_name='Site URL')),
                ('thumbnail', models.URLField(verbose_name='Site THUMB')),
                ('author', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
