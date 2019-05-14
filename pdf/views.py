from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import UserTranscriptForm, UserComplaintsForm


# Create your views here.
@login_required()
def transcript_view(request):
    if request.method == 'POST':
        get_sem = request.POST.get('my_sem')
        # my_transcript = Transcript.objects.filter(semester_id=get_sem).filter(user_id=request.user.id)
        print(get_sem)

    form = UserTranscriptForm()
    context = {
        'form': form,
        # 'my_transcript': my_transcript
    }

    return render(request, 'transcript.html', context)


@login_required()
def complaint_view(request):
    if request.method == 'POST':
        form = UserComplaintsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'complaint created successfully!')
            return redirect('index')
    else:
        form = UserComplaintsForm()

    context = {
        'form': form,
    }

    return render(request, 'complaint.html', context)
