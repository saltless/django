from django.shortcuts import render
from books.models import Publisher

def bookList(request):
	names = Publisher.objects.all()
	return render(request, 'BookList.html', locals())