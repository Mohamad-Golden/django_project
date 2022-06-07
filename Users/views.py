from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfile, EditUser
from django.contrib.auth.models import User
import os
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            username = request.POST['username']
            password = request.POST['password1']
            messages.success(request, f'An account is created with username "{username} {password}"')
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'Users/register.html', {'form':form})


class RegisterView(FormView):
    template_name = 'Users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog-home')

    def form_valid(self, *args, **kwargs):
        args[0].save()
        username = self.request.POST['username']
        messages.success(self.request, f'An account is created with username "{username}"')
        return super().form_valid(self)

    def form_invalid(self,form):
        # print(str(form.errors))
        if 'unique' in str(form.errors):
            print('hello wordl')
            messages.error(self.request, f"نام کاربری {self.request.POST.get('username')} گرفته شده است")
        return super().form_invalid(form)

@login_required
def profile(request):
    if request.method == "POST":
        old_img = request.user.profile.image.path
        u_form = EditUser(request.POST, instance=request.user)
        p_form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            if os.path.basename(old_img) != 'default.jpg':
                os.remove(old_img)

            messages.success(request, 'your profile is updated!')
            return redirect('users-profile')

    u_form = EditUser(instance=request.user)
    p_form = EditProfile(instance=request.user.profile)
    return render(request, 'Users/profile.html', {'u_form':u_form, 'p_form':p_form})


def re_home(request):
    return redirect('blog-home')