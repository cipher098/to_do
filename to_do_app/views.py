from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Work
from .forms import WorkForm
from django.contrib import messages

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

# def send_notification_mail():
# 	subject = 'WORK DUE!!!'
# 	message = ''
# 	from_email = ''
# 	recipient_email = ['']
# 	send_mail(subject,
# 		message,
# 		from_email,
# 		recipient_email,
# 		fail_silently=False
# 	)
# 	to_email = kwargs.get('to_email')
#     from_email = 'notify@todo.com>'
#     subject = get_cleaned_email_subject('Work Due.')
#     link = settings.API_DOMAIN_ROOT + str(reverse('auth:verify-email',
#                                                   args=[activation_key,
#                                                         user_type]))

#     message = 'Your work is due today.'
#     user_name = kwargs.get('user_name', '')
#     button_text = 'Verify'
#     button = get_html_email_button_dict(link, button_text)
#     msg_plain, msg_html = get_rendered_email(user_name, message, button)

#     try:
#         send_mail(
#             subject,
#             msg_plain,
#             from_email,
#             [to_email],
#             html_message=msg_html,
#         )
#     except:
#         return function_response(False, 'Email could not be sent')

#     return function_response(True, 'Email successfully sent')
# send_booking_user_mail(**user_kwargs)