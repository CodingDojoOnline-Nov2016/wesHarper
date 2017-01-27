from __future__ import unicode_literals

from django.db import models
from django.db.models import Count

import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def create_user(self, alias, first, last, email, pw_hash):
		user = self.create(
			alias=alias,
			first_name=first,
			last_name=last,
			email=email,
			pw_hash=pw_hash
		)
		return user

	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_pw

	def compare_passwords(self, user, password):
		password = password.encode()
		hashed_pw = user.pw_hash.encode()
		if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
			return True
		else:
			return False

	def validate_and_register(self, data):
		#unpack data
		alias = data['alias']
		first = data['first-name']
		last = data['last-name']
		email = data['email']
		password = data['password']
		confirm = data['confirm']
		#initialize error handler
		errors = []
		#run form validations
		if len(alias) < 1:
			errors.append('Please enter an alias')
		elif not alias.isalpha():
			errors.append('Alias must contain only letters, sorry!')
		if len(first) < 1:
			errors.append('Please enter a first name')
		elif not first.isalpha():
			errors.append('First name must contain only letters, sorry!')
		if len(last) < 1:
			errors.append('Please enter a last name')
		elif not last.isalpha():
			errors.append('Last name must contain only letters, sorry!')
		if len(email) < 1:
			errors.append('Please enter an email address')
		elif not EMAIL_REGEX.match(email):
			errors.append('Please enter a valid email address')
		if len(password) < 8:
			errors.append('Password must be at least 8 characters')
		elif password != confirm:
			errors.append("Passwords don't match")
		#break out if there are errors
		if errors:
			return (False, errors)

		try:
			match = self.get(email=email)
			errors.append("A user already exists with that email, please login or sign up with a new email.")
			return (False, errors)
		except:
			#once every check passes, hash password
			pw_hash = self.hash_password(password)
			#once password is hashed, create user
			user = self.create_user(alias, first, last, email, pw_hash)
			return (True, user)

	def login_check(self, data):
		#unpack data
		email = data['email']
		password = data['password']
		#initialize error handler
		errors = []
		try:
			user = self.get(email=email)
			if self.compare_passwords(user, password):
				return (True, user)
		except:
			errors.append("Incorrect email or password")

		return(False, errors)

	def get_user_info(self, user_id):
		user_id = int(user_id)
		try:
			user = self.get(id=user_id)

			response = {
				'alias': user.alias,
				'first_name': user.first_name,
				'last_name': user.last_name,
				'email': user.email,
				# 'total_reviews': self.filter(id=user_id).annotate(total_reviews=Count('user_review')),
				# 'books': self.filter(id=user_id).filter(review_user__review_book)
			}
			return (True, response)
		except:
			errors = "There was a problem loading this user."
			return (False, errors)

class User(models.Model):
	alias = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()