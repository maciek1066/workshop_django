from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .forms import TweetForm, AddTweetForm
from .models import Tweet
from django.contrib.auth.models import User

# Create your views here.


# class BaseView(View):
#     def get(self, request):
#         return render(request, "base.html", {})


class InheritView(View):
    def get(self, request):
        return render(request, "son_of_base.html", {})


class DisplayTweets(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        ctx = {
            "tweets": tweets
        }
        return render(request,
                      template_name="base.html",
                      context=ctx
                      )


class AddTweetView(View):
    def get(self, request):
        form = AddTweetForm()
        ctx = {
            "form": form
        }
        return render(request,
                      template_name="add_tweet.html",
                      context=ctx
                      )

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = form.cleaned_data['user']
            Tweet.objects.create(content=content, user=user)
            return redirect("/")
        ctx = {
            "form": form
        }
        return render(request,
                      template_name="add_tweet.html",
                      context=ctx
                      )

# class TweetView(View):
#
#     def get(self, request):
#         form = TweetForm()
#