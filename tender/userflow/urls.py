from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'userflow'
urlpatterns = [
    path('test', views.test, name='test'),
    path('onboarding', views.onboarding, name='onboarding'),
    path('experience', views.experience, name='experience'),
    path('symptom/new', views.symptom_new, name='symptom_new'),
    path('symptom/result', views.symptom_result, name='symptom_result'),
    path('report', views.report, name='report'),
]