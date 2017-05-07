# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Review, Therapist
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def therapist_list(request):
    therapist_list = Therapist.objects.order_by('-name')
    context = {'therapist_list':therapist_list}
    return render(request, 'reviews/therapist_list.html', context)


def therapist_detail(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    return render(request, 'reviews/therapist_detail.html', {'therapist': therapist})

@login_required
def add_review(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.therapist = therapist
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:therapist_detail', args=(therapist.id,)))

    return render(request, 'reviews/therapist_detail.html', {'therapist': therapist, 'form': form})
