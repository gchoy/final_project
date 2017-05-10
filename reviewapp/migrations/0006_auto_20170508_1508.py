# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 22:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewapp', '0005_cluster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='therapist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='therapist',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='therapist',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='therapist',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='tags',
            field=models.ManyToManyField(blank=True, to='reviewapp.Tag'),
        ),
    ]