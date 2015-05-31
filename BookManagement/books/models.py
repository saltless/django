from django.db import models

class Publiser(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 50)
	city = models.CharField(max_length = 60)
	state = models.CharField(max_length = 30)
	country = models.CharField(max_length = 50)
	website = models.URLField()

class Author(models.Model):
	firstName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 40)
	email = models.EmailField()

class Book(models.Model):
	title = models.CharField(max_length = 100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publiser)
	publicationData = models.DataField()

