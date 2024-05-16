from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.SignUpPage,name='signup'),
    path('login/',views.LoginPage,name ='login'),
    path('home/',views.HomePage,name ='home'),
    path('logout/',views.LogOutPage,name = 'logout'),
    
    # Reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    

]