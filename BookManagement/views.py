from django.shortcuts import render
from 

def bookList(request):
	db = MySQLdb.connect(user = 'root', db = 'bankSystem', passwd = 'r7hbz6x', host = 'localhost')
	cursor = db.cursor()
	cursor.execute('select * from company order by city')
	names = [row[0] for row in cursor.fetchall()]
	db.close()
	return render(request, 'BookList.html', locals())