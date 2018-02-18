from django import forms
from cinema.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    error_message = {'password_mismatch': 'Two password field didnt match'}
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput,
        help_text="Enter the same passowrd as above")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password1 and password2 does not match"
            )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'phone_number', 'location')


class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangeForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput, help_text='Enter the same Password as above')
    error_message = {'password_mismatch': 'Two Passowrd Field Didnt match'}

    class Meta:
        model = User
        fields = ('username', )

    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        Password1 = cleaned_data['password1']
        Password2 = cleaned_data['password2']
        if Password1 != Password2:
            raise forms.ValidationError(
                self.error_message['password_mismatch'], code='password_mismatch')
            return Password2
