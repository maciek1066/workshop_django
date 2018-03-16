from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email

from .models import Tweet

users = User.objects.all()


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'


class AddTweetForm(forms.Form):
    content = forms.CharField(label="Content")
    user = forms.ModelChoiceField(queryset=users)

