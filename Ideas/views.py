from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Idea, Customer
from .forms import IdeaForm, UserForm
from django.contrib.auth import login
from django.contrib import messages
 
# Create your views here.
def indexPageView(request):
    return render(request, 'ideas/index.html')

def registerPageView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            messages.success(request, "Registration Successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm()
    return render (request=request, template_name="ideas/register.html", context={"register_form":form})

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

def ideasPageView(request, pk):
    customer = Customer.objects.get(id=pk)

    first_name = customer.first_name

    context = {'customer':customer, 'first_name':first_name}
    return render(request, 'ideas/ideas.html', context) # page for after the user logs in