from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'ideas/index.html')
def aboutPageView(request):
    return render(request, 'ideas/about.html')
def uploadPageView(request):
    return HttpResponse('Upload new ideas here!')
def ideasPageView(request, fName, lName):
    return HttpResponse(f'<h2>Welcome {fName} {lName}!</h2>') # page for after the user logs in