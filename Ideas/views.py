from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse('<h1>Welcome to Sifty!</h1>')
def aboutPageView(request):
    return HttpResponse('About Sifty')
def uploadPageView(request):
    return HttpResponse('Upload new ideas here!')
def ideasPageView(request, fName, lName):
    return HttpResponse(f'<h2>Welcome {fName} {lName}!</h2>') # page for after the user logs in