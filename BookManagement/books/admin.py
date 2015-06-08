from django.contrib import admin
from books.models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('firstName', 'lastName', 'email')
	search_fields = ('firstName', 'lastName')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publicationDate')
	list_filter = ('publicationDate', 'authors')
	date_hierarchy = 'publicationDate'
	ordering = ('-publicationDate', )
	filter_horizontal = ('authors', )
#	raw_id_fields = ('publisher', )

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)