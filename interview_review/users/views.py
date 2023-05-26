from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy


class SignUp(generic.View):

    def get(self, request):
        return render(request, 'users/sign_up.html')

    def post(self, request):
        ...


class SignIn(generic.View):

    def get(self, request):
        return render(request, 'users/sign_in.html')

    def post(self, request):
        ...


class Profile(generic.View):

    def get(self, request):
        ...

    def post(self, request):
        ...


class ResetPassword(generic.View):

    def get(self, request):
        ...

    def post(self, request):
        ...