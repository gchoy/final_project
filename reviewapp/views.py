# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from .models import Review, Therapist


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'revies/review_detail.html', {'review': review})


def therapist_list(request):
    therapist_list = Therapist.objects.order_by('-name')
    context = {'therapist_list':therapist_list}
    return render(request, 'reviews/therapist_list.html', context)


def therapist_detail(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    return render(request, 'reviews/therapist_detail.html', {'therapist': therapist})
