from django.urls import path

from pdf import views

urlpatterns = [
    path('transcript/', views.transcript_view, name='transcript'),
    path('complaints/', views.complaint_view, name='complaints'),
]
