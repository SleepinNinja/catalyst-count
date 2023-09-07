from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email')


class CreateNewUserForm(forms.ModelForm):
	password = forms.CharField(max_length=30)
	confirm_password = forms.CharField(max_length=30)

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean(self):
		cleaned_data = super(CreateNewUserForm, self).clean()
		if cleaned_data.get('username').strip() in [None, '']:
			raise ValidationError('Please provide a username')
		if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
			raise ValidationError('Password dont match')
		return cleaned_data

	def save(self, commit=True):
		new_user = super(CreateNewUserForm, self).save(commit=False)
		cleaned_data = self.cleaned_data
		new_user.set_password(cleaned_data.get('password'))
		if commit:
			new_user.save()
		return new_user
		#new_user.set_password()