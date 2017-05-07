from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /reviews/id/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /therapist/
    url(r'^therapist$', views.therapist_list, name='therapist_list'),
    # ex: /therapists/id/
    url(r'^therapist/(?P<therapist_id>[0-9]+)/$', views.therapist_detail, name='therapist_detail'),
    url(r'^therapist/(?P<therapist_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
