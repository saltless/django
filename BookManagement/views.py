from django.shortcuts import render
from django.http import HttpResponse
from books.models import Publisher, Book

def bookList(request):
	names = Publisher.objects.all()
	return render(request, 'BookList.html', locals())

def requestTest(request):
	metaInfo = request.META.items()
	metaInfo.sort()
	return render(request, 'MetaList.html', locals())

def search(request):
	errors = []
	if 'bookname' in request.GET: 
		bookname = request.GET['bookname']
		if not bookname:
			errors.append('Please enter a valid book name.')
		elif len(bookname) > 20:
			errors.append('Please enter a valid book name less then 20 characters.')
		else:
			books = Book.objects.filter(title__icontains = bookname)
			return render(request, 'searchResult.html', locals())
	return render(request, 'searchForm.html', locals())

