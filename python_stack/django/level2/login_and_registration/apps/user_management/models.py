from __future__ import unicode_literals
from django.db import models

import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	#define user creation for use in other models functions
	def create_user(self, first, last, email, pw_hash):
		user = self.create(first_name=first, last_name=last, email=email, pw_hash=pw_hash)
		return user

	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		# print hashed_pw
		return hashed_pw

	def login_check(self, data):
		#initialize error handler
		errors=[]
		#unpack data
		email = data['email']
		password = data['password'].encode()
		#run validations
		try:
			user = self.get(email=email)
			hashed_pw = user.pw_hash.encode()
			if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
				return (True, user)
		except:
			errors.append("Incorrect email or password")
		
		return (False, errors)

	def validate_and_add(self, data):
		#initialize error handler
		errors = []
		#unpack data
		first = data['first-name']
		last = data['last-name']
		email = data['email']
		password = data['password']
		confirm = data['confirm']
		#run validations
		if len(first) < 2:
			errors.append("Please enter a first name.")
		elif not first.isalpha():
			errors.append("Please enter a valid first name.")
		if len(last) < 2:
			errors.append("Please enter a last name.")
		elif not last.isalpha():
			errors.append("Please enter a valid last name.")
		if len(email) < 1:
			errors.append("Please enter an email address.")
		elif not EMAIL_REGEX.match(email):
			errors.append("Please enter a valid email address.")
		if len(password) < 8:
			errors.append("Please enter a valid password.")
		elif password != confirm:
			errors.append("Passwords must match")

		if not errors:
			#Once form is validated, check to see if user exists.
			try:
				matches = self.get(email=email)
				errors.append("A user already exists with that email.")
				return (False, errors)
			except:
				#if all else passes hash password
				pw_hash = self.hash_password(data['password'])
				#create user with hashed password
				user = self.create_user(data['first-name'], data['last-name'], data['email'], pw_hash)
				return (True, user)
		else:
			print "triggered w/errors"
			return (False, errors)


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()