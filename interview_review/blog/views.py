from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy


class ShowMainPage(generic.TemplateView):
    template_name = 'blog/home.html'
