from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


from .forms import UserRegistrationForm


User = get_user_model()



class UserLogin(LoginView):
    template_name = 'login.html'


    def get_success_url(self):
        return self.request.POST.get('next')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)



def user_logout(request):
    logout(request)
    return redirect('login')



class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)


