from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account', views.account_func, name='account'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),

    
]
