from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ideas.models import Idea, Customer
from .forms import IdeaForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
 
# Create your views here.
def indexPageView(request):
    customer_ideas = Idea.objects.filter(customer = request.user.id)
    # customer = Customer.objects.get(personID = request.user.id)
    # first_name = customer.first_name
    # last_name = customer.last_name

    context = {'customer_ideas':customer_ideas}#, 'first_name':first_name, 'last_name':last_name}
    
    return render(request, 'ideas/index.html', context)

def registerPageView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            messages.success(request, "Registration Successful.")
            return redirect("add_info")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm()
    return render (request=request, template_name="ideas/register.html", context={"register_form":form})

def loginPageView(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="ideas/login.html", context={"login_form":form})

def logoutPageView(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def addInfoPageView(request):
    if request.method == "POST":
        customer = Customer()

        customer.personID = User.objects.get(id = request.user.id)
        customer.first_name = request.POST["first_name"]
        customer.last_name = request.POST["last_name"]
        
        customer.save()

        return redirect("index")
    return render(request, 'ideas/add_info.html')

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
    customer_ideas = Idea.objects.filter(customer = request.user.id)
    customer = Customer.objects.get(personID = request.user.id)
    first_name = customer.first_name
    last_name = customer.last_name

    context = {'customer_ideas':customer_ideas, 'first_name':first_name, 'last_name':last_name}
    
    return render(request, 'ideas/ideas.html', context) # page for after the user logs in

def updateIdeaPageView(request, pk):
    idea = Idea.objects.get(id=pk)
    form = IdeaForm(instance=idea)

    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'ideas/update_idea.html', context)

def deleteIdeaEntry(request, idea_id):
    entry = Idea.objects.get(idea_id = idea_id)
    entry.delete()
    return redirect('ideas')