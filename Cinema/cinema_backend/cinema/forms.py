from django import forms
from cinema.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

	error_message={
	'password_mismatch' :'Two password field didnt match',
	}
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput, help_text="Enter the same passowrd as above")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_password2(self):
		password1 = self.cleaned_data.get("Password1")
		password2 = self.cleaned_data.get("Password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_message['password_mismatch'], code = 'password_mismatch'
					)
		return password2



class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'phone_number', 'location')


class UserUpdateForm(forms.ModelForm):

	username = forms.CharField(widget = forms.TextInput(attrs = {'readonly' : 'readonly'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)


class PasswordChangeForm(forms.ModelForm):
	password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label = "Password Confirmation", widget=forms.PasswordInput, help_text='Enter the same Password as above')
	error_message= {

	'password_mismatch' : 'Two Passowrd Field Didnt match'
	}

	class Meta:
		model = User
		fields = ('username', )

	def clean_password(self):
		Password1 = self.cleaned_data['password1']
		Password2 = self.cleaned_data['password2']
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
					self.error_message['password_mismatch'], code = 'password_mismatch'
				)
			return password2