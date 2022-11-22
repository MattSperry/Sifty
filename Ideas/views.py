from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Idea
from .forms import IdeaForm
 
# Create your views here.
def indexPageView(request):
    return render(request, 'ideas/index.html')

def aboutPageView(request):
    return render(request, 'ideas/about.html')

def uploadPageView(request):
    data = Idea.objects.all()
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = IdeaForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'ideas/uploads.html', context)

def ideasPageView(request):
    return render(request, 'ideas/ideas.html') # page for after the user logs in