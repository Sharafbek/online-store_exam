from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView



from . import views

urlpatterns = [

    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('account', views.account_func, name='account'),

    
]
