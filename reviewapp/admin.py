# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Therapist, Review, Tag, Cluster
from reviewapp.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('therapist','rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name','rating']
    search_fields = ['comment']

class TherapistAdmin(admin.ModelAdmin):
    model = Therapist
    list_display = ['name']
    list_filter = ['tags', 'users','tags']
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['tag']

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Cluster, ClusterAdmin)
