# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 03:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarked_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('channel_title', models.CharField(max_length=30)),
                ('channel_id', models.CharField(default='none', max_length=30)),
                ('video_id', models.CharField(max_length=30)),
                ('published_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoInfo'),
        ),
    ]
