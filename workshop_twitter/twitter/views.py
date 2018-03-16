from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, "base.html", {})


class InheritView(View):
    def get(self, request):
        return render(request, "son_of_base.html", {})
