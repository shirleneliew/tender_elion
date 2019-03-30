from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('onboarding', views.onboarding),
    path('experience', views.experience),
    path('symptom/new', views.symptom_new),
    path('symptom/result', views.symptom_result),
    path('report', views.report),
]