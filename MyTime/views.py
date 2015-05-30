from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime

def hello(request):
	return HttpResponse("Hello World!")

def currTime(request):
	time = datetime.datetime.now()
	return render(request, 'TimeTemplateCurrent.html', locals())

def hoursAhead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise http404()
	time = datetime.datetime.now() + datetime.timedelta(hours = offset)
	return render(request, 'TimeTemplateFuture.html', locals())
