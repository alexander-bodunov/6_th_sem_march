__author__ = 'Work'
from django import forms
from django.contrib.auth.models import User
from . import models
#from .middleware import get_current_user
from datetime import datetime

class FormRegister(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'],
                                        )
        return user

class FormAuth(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class FormUserProfileEdit(forms.Form):
    photo=forms.IntegerField()
    def save(self,request):
        profile=models.UserProfile.objects.create(
            user=request.user.pk,
            photo=self.cleaned_data['photo'],
            user_id=request.user,
        )
        return profile

class FormUserWallEdit(forms.Form):
    title=forms.CharField()
    text=forms.CharField()
    is_commentable=forms.BooleanField()
    def save(self,request):
        record=models.Wall.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            posted=datetime.now(),
            is_commentable=self.cleaned_data['is_commentable'],
            my_user=request.user.pk, #models.UserProfile.objects.filter(pk=request.user.pk)
            user_id=request.user
        )
        return record

class MessageAdd(forms.Form):
    to_user=forms.IntegerField()
    text=forms.CharField()
    def save(self,request):
        models.Message.objects.create(
            from_user=request.user.pk,
            to_user=self.cleaned_data['reciever'],
            text=self.cleaned_data['text'],
            send_date=datetime.now(),
            resieved_date=datetime.now(),
            _from_user_id=request.user,
            _to_user_id=self.cleaned_data['reciever'],
    )

class FriendAdd(forms.Form):
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range','min':0 ,'max':100, 'step': '2'}))