from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
	#making query
	tasks = Task.objects.all() 

	form = TaskForm()

	if request.method == 'POST':
		#we want to create new form
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request,'tasks/list.html',context)