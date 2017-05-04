# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Therapist, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('therapist', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Therapist)
admin.site.register(Review, ReviewAdmin)
