from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'ideas/index.html')

def aboutPageView(request):
    return render(request, 'ideas/about.html')

def uploadPageView(request):
    return render(request, 'ideas/uploads.html')

def ideasPageView(request, fName, lName):
    return render(request, 'ideas/ideas.html') # page for after the user logs in