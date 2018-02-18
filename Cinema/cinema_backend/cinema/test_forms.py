from django.test import TestCase
from .forms import UserForm, ProfileForm, UserUpdateForm, PasswordChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'username': 'bindeep',
            'first_name': 'Bindeep',
            'last_name': 'Acharya',
            'email': 'a@b.com',
            'password1': 'bindeep123',
            'password2': 'bindeep123'
        }
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data.get('email'), 'a@b.com')

    def test_invalid_form(self):
        data = {
            'username': 'raj',
            'first_name': 'Bindeep',
            'last_name': 'Acharya',
            'email': 'a@b.com',
            'password1': 'alal ',
            'password2': 'popoop'
        }
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        print(form.errors)


class ProfileFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'gender': 'Male',
            'phone_number': '12345',
            'location': 'kathmandu'
        }
        form = ProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'gender': 'Male',
            'phone_number': 'aoaopap',
            'location': 'kathmandu'
        }
        form = ProfileForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        print(form.errors)


class UserUpdateFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'username': 'bindeep',
            'first_name': 'Bindeep',
            'last_name': 'Acharya',
            'email': 'a@b.com'
        }
        form = UserUpdateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'username': 'bindeep',
            'first_name': 'Bindeep',
            'last_name': 'Acharya',
            'email': 'ppppp'
        }
        form = UserUpdateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        print(form.errors)


class PasswordChangeFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'username': 'bindeep',
            'password1': 'bindeep1',
            'password2': 'bindeep1'
        }
        form = PasswordChangeForm(data=data)
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_invalid_form_without_username(self):
        data = {
            'password1': 'bindeep1',
            'password2': 'bindeep1'
        }
        form = PasswordChangeForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        print(form.errors)

    def test_invalid_form_with_password_mismatch(self):
        data = {
            'username': 'bindeep',
            'password1': 'bindeep1',
            'password2': 'bindeep123'
        }
        form = PasswordChangeForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        print(form.errors)
