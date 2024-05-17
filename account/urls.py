from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns=[
    path('', views.SignUpPage,name='signup'),
    path('login/',views.LoginPage,name ='login'),
    path('home/',views.HomePage,name ='home'),
    path('logout/',views.LogOutPage,name = 'logout'),
    path('add_product/', add_product, name='add_product'),
    path('my_products/', user_products, name='user_products'),
    path('edit_product/<int:product_id>', edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
   
    
    # Reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('ChangePassword/',views.Change_Password,name ='ChangePassword'),
    

]