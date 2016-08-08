# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import bcrypt

#Our new manager!
class UserManager(models.Manager):
def login(self, email, password):
	print "Running a login function!"
	print "If successful login occurs, maybe return a tuple with (True, user) where user is a user object?)"
	print "If unsuccessful, maybe return a tuple with (False, 'Login unsuccessful')"
	pass
def register(self, **kwargs):
	print ("Register a user here")
	errors = []
	first_name = kwargs['first_name']
	last_name = kwargs['last_name']
	password = kwargs['password']
	if not first_name:
		errors.append('first name must be filled')
	if not last_name:
		errors.append('last name must be filled')
	if not email:
		errors.append('email must be filled')
		if not email_regex.match(email):
			errors.append('email must be valid')
	if len(errors):
		return (False, errors)
	else:
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(15))
		print hashed_pw
		User.objects.create(first_name=first_name, last_name=last_name, password=hashed_pw)

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
