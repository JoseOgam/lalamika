from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'home.html', )


@login_required()
def index_view(request):
    return render(request, 'index.html')
