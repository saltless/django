from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 50)
	city = models.CharField(max_length = 60)
	state = models.CharField(max_length = 30)
	country = models.CharField(max_length = 50)
	website = models.URLField()

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Author(models.Model):
	firstName = models.CharField(max_length = 30, verbose_name = 'first name')
	lastName = models.CharField(max_length = 40, verbose_name = 'last name')
	email = models.EmailField(blank = True, verbose_name = 'e-mail')

	def __unicode__(self):
		return u'%s %s' %(self.firstName, self.lastName)

class Book(models.Model):
	title = models.CharField(max_length = 100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publicationDate = models.DateField(blank = True, null = True, verbose_name = 'publication date')

	def __unicode__(self):
		return self.title
