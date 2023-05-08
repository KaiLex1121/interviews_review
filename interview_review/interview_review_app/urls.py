from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShowMainPage.as_view(), name='show_main_page'),
]
