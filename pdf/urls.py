from django.urls import path

from pdf import views

urlpatterns = [
    path('transcript/<int:id>', views.transcript_view, name='transcript'),
    path('complaints/<int:id>', views.complaint_view, name='complaints'),
]
