from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin



class RegisterView(UserPassesTestMixin, CreateView): 
    form_class = UserRegisterForm 
    template_name = 'registration/register.html'

    def test_func(self) -> bool | None:
        us = self.request.user.is_anonymous
        if us: 
            return False 
    
    def get_success_url(self) -> str:
        login(self.request, self.object) 
        return reverse_lazy('Courses_list')

@login_required
def edit_profile(request): 
    if request.method == 'POST': 
        form = ProfileForm(request.POST ,instance=request.user) 
        if form.is_valid(): 
            form.save()
            return redirect('profile')
    else: 
        form = ProfileForm(instance=request.user)
        return render(request,'profile.html', {
            'form':form
        })