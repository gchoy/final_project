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
    # /review/user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^review/(?P<review_id>[0-9]+)/user/(?P<username>\w+)/edit/$', views.edit_review, name='edit_review'),
    url(r'^about/$', views.about, name='about'),
    url(r'^welcome/$', views.welcome, name='welcome'),
]
