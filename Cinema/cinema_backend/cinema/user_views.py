from .models import UserProfile
from .forms import UserForm, ProfileForm, UserUpdateForm, PasswordChangeForm
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class UserRegisterView(View):
    user_form_class = UserForm
    profile_form_class = ProfileForm
    template_name = 'user/user_registration.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)

        context = {

            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)


@method_decorator(csrf_protect)
def post(self, request):
    user_created_form = self.user_form_class(request.POST)
    profile_form = self.profile_form_class(request.POST)

    if user_created_form.is_valid() and profile_form.is_valid():
        username = user_created_form.cleaned_data['username']
        firstname = user_created_form.cleaned_data['first_name']
        lastname = user_created_form.cleaned_data['last_name']
        email = user_created_form.cleaned_data['email']
        password = user_created_form.cleaned_data['password1']
        gender = profile_form.cleaned_data['gender']
        phone_number = profile_form.cleaned_data['phone_number']
        location = profile_form.cleaned_data['location']

        try:
            with transaction.atomic():
                created_user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=firstname,
                    last_name=lastname,
                    email=email
                )
                profile = UserProfile.objects.create(
                    owner=created_user,
                    gender=gender,
                    phone_number=phone_number,
                    location=location
                )
                created_user.save()
                profile.save()
                return redirect('movie:movie-list')
        except:
            return render(request, self.template_name, {

                'user_form': user_created_form,
                'profile_form': profile_form,
                'error': 'retry'})


class UserUpdateView(View):
    template_name = 'user/update.html'

    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)

        context = {

            'user_form': user_form,
            'profile_form': profile_form,
            'Update': 'Update'
        }
        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    def post(self, request):
        user_created_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_created_form.is_valid() and profile_form.is_valid():
            username = user_created_form.cleaned_data['username']
            firstname = user_created_form.cleaned_data['first_name']
            lastname = user_created_form.cleaned_data['last_name']
            email = user_created_form.cleaned_data['email']
            gender = profile_form.cleaned_data['gender']
            phone_number = profile_form.cleaned_data['phone_number']
            location = profile_form.cleaned_data['location']
            try:
                with transaction.atomic():
                    Created_user = User.objects.get(username=username)
                    Created_user.email = email
                    Created_user.first_name = firstname
                    Created_user.last_name = lastname
                    Created_user.userprofile.gender = gender
                    Created_user.userprofile.phone_number = phone_number
                    Created_user.userprofile.location = location
                    Created_user.save()
                    return redirect('movie:user_detail')

            except:
                return render(request, self.template_name, {

                    'user_form': user_created_form,
                    'profile_form': profile_form,
                    'error': 'retry'
                })


class UserProfileView(View):
    template_name = 'user/detail.html'

    def get(self, request):
        args = {
            'user': request.user
        }
        return render(request, self.template_name, args)


class PasswordChangeView(View):
    template_name = 'user/detail.html'

    def get(self, request):
        change_form = PasswordChangeForm(None)
        context = {

            'form': change_form
        }
        return render(request, 'user/change_password.html', context)

    @method_decorator(csrf_protect)
    def post(self, request):
        change_form = PasswordChangeForm(request.POST, instance=request.user)

        if change_form.is_valid():
            username = change_form.cleaned_data['username']
            password = change_form.cleaned_data['password2']

            try:
                created_user = User.objects.get(username=username)
                created_user.set_password(password)
                created_user.save()
                return render(
                    request,
                    'user/detail.html',
                    {'message': 'Your Password Has been Changed Successfully'})

            except:
                return render(request, 'user/change_password.html', {
                    'form': 'change_form',
                    'message': 'Password Change is unsuccessful'
                })
