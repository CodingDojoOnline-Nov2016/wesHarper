from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
	def validate_email(self, email):
		# define regex pattern
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		# initialize error handler
		errors = []
		# run validations
		if not EMAIL_REGEX.match(email):
			errors.append('Please enter a valid email address.')
			return (False, errors)
		else:
			return (True, email)

class User(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()