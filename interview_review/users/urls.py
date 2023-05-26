from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.SignUp.as_view(), name='sign_up_page'),
    path('sign_in/', views.SignIn.as_view(), name='sign_in_page'),
    path('profile/', views.Profile.as_view(), name='profile_page'),
    path('reset_password', views.ResetPassword.as_view(), name='reset_password_page')
]