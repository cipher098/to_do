from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Work
from .forms import WorkForm
from django.contrib import messages

import time
import datetime
import celery

ToDo_params = [
			   'work',
			   'due_time',
			   'priority',	
			   'completed',
			   'created_time',
			  ]

def delete(request, work_id):
	try:
		work_object = Work.objects.get(id=work_id)
	except:
		return function_response(True, 'Work with given id not found.')	
	work_object.delete()
	messages.success(request, ('Item has been deleted.'))
	return redirect('home')

def home(request):
	if request.method == 'POST':
		parameter_dictionary = request.POST
		work_object = Work()
		if (parameter_dictionary['due_time'] != ''):
			work_object.due_time = parameter_dictionary['due_time']
		work_object.work = parameter_dictionary['work']
		if (parameter_dictionary['priority'] != ''):
			work_object.priority = parameter_dictionary['priority']
		work_object.save()
		messages.success(request, ('Item has been added to list!'))
		all_items = Work.objects.all
		return render(request, 'home.html', {'all_items': all_items})
	else:
		all_items = Work.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def cross_off(request, work_id):
	item = Work.objects.get(pk=work_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, work_id):
	item = Work.objects.get(pk=work_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request, work_id):
	if  request.method == 'POST':
		parameter_dictionary = request.POST
		work_object = Work.objects.get(id=work_id)
		for i in ToDo_params:
			if(parameter_dictionary[i] != ''):
				setattr(work_object, i, parameter_dictionary[i])
		work_object.save()
		messages.success(request, ('Item has been edited!'))
		return redirect('home')
	else:
		item = Work.objects.get(pk=work_id)
		return render(request, 'edit.html', {'item': item})

@celery.decorators.periodic_task(run_every=datetime.timedelta(hours=10))
def check_work_status():
	current_time = datetime.datetime.now()
	work_objects = Work.objects.filter(completed=False,due_time__lt=current_time).order_by('-due_time')
	for item in work_objects:
		item.completed = True
		item.save()
	return
