# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import bcrypt, re
email_regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
#Our new manager!
class UserManager(models.Manager):
	def login(self, email, password):
		print "Running a login function!"
		print "If successful login occurs, maybe return a tuple with (True, user) where user is a user object?)"
		print "If unsuccessful, maybe return a tuple with (False, 'Login unsuccessful')"
		pass
	def register(self, **kwargs):
		print ("Registering a user here")
		errors = []
		first_name = kwargs['first_name']
		last_name = kwargs['last_name']
		email = kwargs['email']
		password = kwargs['password'][0]
		if not first_name:
			errors.append('first name must be filled')
		if not last_name:
			errors.append('last name must be filled')
		if not email:
			errors.append('email must be filled')
			if not email_regex.match(email):
				errors.append('email must be valid')
		if not password:
			errors.append('password must be filled')
		if len(errors):
			return (False, errors)
		else:
			print type(password)
			print password
			hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
			print hashed_pw
			user = User.objects.create(first_name=first_name, last_name=last_name, password=hashed_pw)
			return (True, user)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# *************************
	# Connect an instance of UserManager to our User model!
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************
