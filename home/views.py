from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pdf.models import Transcript


# Create your views here.
def home_view(request):
    return render(request, 'home.html', )


@login_required()
def index_view(request):
    transcripts = Transcript.objects.filter(user=request.user)
    context = {
        'transcripts': transcripts
    }
    return render(request, 'index.html', context)
