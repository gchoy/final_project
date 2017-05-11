# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .models import Review, Therapist,Cluster
from .forms import ReviewForm
from .filters import TherapistFilter
from .suggestions import update_clusters

import datetime

def welcome(request):
    return render(request, 'reviews/welcome.html')

@login_required
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

@login_required
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

@login_required
def therapist_list(request):
    therapist_list = Therapist.objects.order_by('-name')
    context = {'therapist_list':therapist_list}
    return render(request, 'reviews/therapist_list.html', context)

@login_required
def therapist_detail(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    return render(request, 'reviews/therapist_detail.html', {'therapist': therapist})

def about(request):
    return render(request, 'reviews/about.html')


@login_required
def add_review(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.therapist = therapist
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        update_clusters()

        return HttpResponseRedirect(reverse('reviews:therapist_detail', args=(therapist.id,)))

    return render(request, 'reviews/therapist_detail.html', {'therapist': therapist, 'form': form})

@login_required
def edit_review(request, review_id, username):
    review = get_object_or_404(Review, pk=review_id)
    therapist = get_object_or_404(Therapist, pk=review.therapist.id)
    if request.method == "POST":

        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            user_name = request.user.username
            review.save()
            update_clusters()
            return HttpResponseRedirect(reverse('reviews:review_detail', args=(review.id,)))
    else:
        form = ReviewForm(instance=post)
    return render(request, 'reviews/review_detail.html', {'review': review, 'form': form})
    
@login_required
def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)

@login_required
def user_recommendation_list(request):

    user_reviews = Review.objects.filter(user_name=request.user.username).prefetch_related('therapist')
    user_reviews_therapist_ids = set(map(lambda x: x.therapist.id, user_reviews))
    therapist_list = Therapist.objects.exclude(id__in=user_reviews_therapist_ids)
    return render(request, 'reviews/user_recommendation_list.html', {'username': request.user.username, 'therapist_list':therapist_list})

@login_required
def search(request):
    t_list = Therapist.objects.all()
    t_filter = TherapistFilter(request.GET, queryset=t_list)
    return render(request, 'reviews/t_list.html', {'filter': t_filter})
