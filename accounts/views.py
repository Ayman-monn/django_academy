from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin



class RegisterView(CreateView): 
    form_class = UserRegisterForm 
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Courses_list')
        return super().dispatch(request, *args, **kwargs)
    
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