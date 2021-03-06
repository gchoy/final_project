# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=30)),
                ('user_title', models.CharField(blank=True, max_length=30)),
                ('user_bio', models.TextField(blank=True, max_length=500)),
                ('user_type', models.IntegerField(blank=True, choices=[(1, 'Patient'), (2, 'Therapist')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
