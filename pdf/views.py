from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import UserTranscriptForm, UserComplaintsForm
from . import models


# Create your views
@login_required()
def transcript_view(request, id):
    transcript = models.Transcript.objects.get(id=id)
    results = models.Result.objects.filter(transcript=transcript)
    context = {
        'transcript': transcript,
        'results': results
    }

    return render(request, 'view_transcript.html', context)


@login_required()
def complaint_view(request, id):
    if request.method == 'POST':
        form = UserComplaintsForm(request.POST)
        if form.is_valid():
            current_user = request.user.id
            title = request.POST.get('title')
            description = request.POST.get('description')
            models.Complaints.objects.create(title=title, description=description, user_id=current_user, transcript_id=id)
            messages.success(request, 'complaint created successfully!')
            return redirect('index')
    else:
        form = UserComplaintsForm()

    context = {
        'form': form,
    }

    return render(request, 'complaint.html', context)
