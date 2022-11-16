from django.shortcuts import render

def ideasPageView(request) :
    return render(request, 'sifty/index.html')

