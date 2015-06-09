from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from contact.forms import ContactForm

def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			info = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@sample.com'),
				['saltles1@gmail.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial = {'subject': 'Type your subject here.'})
	return render(request, 'ContactForm.html', locals())

def contactThanks(request):
	return render(request, 'Thanks.html')