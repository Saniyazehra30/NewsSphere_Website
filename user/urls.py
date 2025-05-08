from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('faqs/',views.faqs),
    path('news/',views.news),
    path('video_news/',views.video_news),
    path('job_news/',views.job_news),
    path('newsdetail/',views.newsdetail),
    path('login/',views.login),
]