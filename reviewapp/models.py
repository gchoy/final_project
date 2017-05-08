# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime
import numpy as np



class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag


class Therapist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField('created date', default=datetime.datetime.now)
    users = models.ManyToManyField(User, blank=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    # user = models.ForeignKey(User, null=True, blank=True)
    # rating = average_rating()

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(lst.join(','))

    def users_(self):
        lst = [x[1] for x in self.users.values_list()]
        return str(lst.join(','))

class Profile(models.Model):
    PATIENT = 1
    THERAPIST = 2
    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (THERAPIST, 'Therapist'),
    )
    #identifier = models.CharField(max_length=40, unique=True)
    #USERNAME_FIELD = 'identifier'
    #REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30, blank=True)
    user_title = models.CharField(max_length=30, blank=True)
    user_bio = models.TextField(max_length=500, blank=True)
    user_type = models.IntegerField(choices=ROLE_CHOICES, default=1,null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#Review model/table schemaL
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    #therapist = models.ForeignKey(User, null=True, related_name=user_type)
    patient = models.ForeignKey(User, null=True)
    therapist = models.ForeignKey(Therapist, null=True)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
