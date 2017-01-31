from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from .models import User

# class RegisterForm(forms.Form):
# 	first_name = forms.CharField(label="First Name", max_length=45)
# 	last_name = forms.CharField(label="Last Name", max_length=45)
# 	email = forms.EmailField(label="Email")
# 	password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
# 	confirm_password = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)

# class LoginForm(forms.Form):
# 	email = forms.EmailField()
# 	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

# Define form validators
def v_len_gt_eight(value):
	if len(value) < 8:
		raise ValidationError(
			'{} must be at least 8 characters'
		)

def v_name_len(value):
	if len(value) < 2:
		raise ValidationError(
			_('Invalid name: %(value)s, must be at least 2 characters'),
			code='Name length invalid',
			params={ 'value': value },
		)
		
# Create forms from models and modify fields
class RegisterForm(forms.ModelForm):
	password = forms.CharField(
		max_length = 100,
		label = "Password",
		widget = forms.TextInput(
			attrs = {
				'placeholder': "password",
				'type': "password",
			}
		)
	)

	confirm_password  =  forms.CharField(
		max_length = 100,
		label = "Confirm Password",
		widget = forms.TextInput(
			attrs = {
				'placeholder': "confirm",
				'type': 'password',
			}
		)
	)

	first_name = forms.CharField(
		validators=[v_name_len],
		label = "First Name",
		widget = forms.TextInput(
			attrs = {
				'placeholder': "Vanilla"
			}
		)
	)

	last_name = forms.CharField(
		validators=[v_name_len],
		label = "First Name",
		widget = forms.TextInput(
			attrs = {
				'placeholder': "Ice"
			}
		)
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']