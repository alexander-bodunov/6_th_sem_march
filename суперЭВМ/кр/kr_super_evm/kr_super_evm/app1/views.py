from . import models
from . import forms
from django.views.generic import View,ListView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.views.generic.edit import ProcessFormView
from django.db.models import Q
import pymysql
#from pymysql import MySQLdb
from django.core.management.base import BaseCommand
from django.core.cache import cache
import random




# Create your views here.

data={
    'user_page':[],
    'wall':[],
}

mess={
    'message':[],
    'pk':1,
    'len':'10',
    'style_num':{'background':'0','message':0,'music':1},
}

friend={
    'friend':[],
    'on':False,
    'form':{},
    'style_num':{'background':'0','message':0,'music':1}
}

background=['iceage1','iceage2','iceage3']
music=['/static/1.mp3','2.mp3','3.mp3','4.mp3']

def get_user_profile(user_id):
    return models.UserProfile.objects.filter(user=user_id)

def get_user_wall(user_id):
    return models.Wall.objects.filter(my_user=user_id)


class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

class UserView(View):
    def get(self,request):
        data['user_page']=[]
        data['wall']=[]
        user=request.user.pk
        for i in get_user_profile(user):
            data['user_page'].append(i)
        for i in get_user_wall(user):
            data['wall'].append(i)
        try:
            got_online=models.UserProfile.objects.filter(user=user)[0]
            got_online.online=True
            got_online.save()
        except (Exception):
            pass
        return render(request,'user.html',data)


class MessagesView(View):
    def get(self,request):
        '''
        if request.method == 'POST':
            for i in models.Message.objects.all():
                all=models.UserAll.objects.filter(user_id=i.to_user)
                if len(all)==0:
                    models.UserAll.objects.create(
                        user_id=i.to_user,
                        messages_resieved=str(i.pk)
                    )
                else:
                    set_of_messages=all[0].messages_resieved
                    if str(i.pk) not in set_of_messages.split(','):
                        all[0].messages_resieved=set_of_messages +','+str(i.pk)
                        all[0].save()
                        '''
        mess['message']=[]
        personal_messages=models.UserAll.objects.filter(user_id=request.user.pk)
        mess['pk']=request.user.pk
        if len(personal_messages)>0:
            ids=personal_messages[0].messages_resieved.split(',')
            mess['len']=len(ids)
            for i in ids:
                messages_recieved=models.Message.objects.filter(id=i)
                mess['message'].append(messages_recieved[0])
                name=models.User.objects.filter(pk= messages_recieved[0].from_user)
                if len(name)>0:
                    name0=name[0].username
                    mess['message'][len(mess['message'])-1].user=name0
                    mess['style_num']['background']=background[random.randint(0,2)]
                    mess['style_num']['message']='nut'
                    mess['style_num']['misic']=random.randint(0,3)

        return render(request,'messages.html',mess)


class FriendsView(View):
    def get(self,request):
        #if request.POST:
        #add_message(request=request)
        if request.method=='POST':
            #form=forms.MessageAdd(request.POST)
            #form.save(request)
            return HttpResponseRedirect('/userPage/friends/')
        form=forms.MessageAdd(request.POST)
        friend['friend']=[]
        friend['form']=form
        all_users=models.User.objects.all()
        for _user in all_users:
            try:
                _user.on=models.UserProfile.objects.filter(user_id_id=_user.pk)[0].online
                _user.is_friend=True
                _user.is_user=4
            except (Exception):
                pass
            friend['friend'].append(_user)
            friend['style_num']['background']=background[random.randint(0,2)]
            #friend['on']=models.UserProfile.objects.filter(user=user.id)[0].online
        return render(request,'friends.html',friend)


class FriendsOnlyView(View):
    def get(self,request):
        form=forms.MessageAdd(request.POST)
        friend['friend']=[]
        friend['form']=form
        all_friends=models.Friend.objects.filter(Q(user_id_1=request.user.pk) | Q(user_id_2=request.user.pk)).order_by("heart1")
        #all_users=models.User.objects.all()
        for _friend in all_friends:
            is_added=_friend.is_friend_status
            heart_rate=_friend.heart1
            _id = {_friend.user_id_1,_friend.user_id_2}-{request.user.pk}
            for i in _id:
                id=i
            user_friend=models.User.objects.filter(id=id)[0]
            try:
                user_friend.on=models.UserProfile.objects.filter(user_id_id=user_friend.pk)[0].online
                user_friend.is_friend=is_added
                user_friend.heart_rate=heart_rate
                user_friend.is_user=2
            except (Exception):
                pass
            friend['friend'].append(user_friend)
            friend['style_num']['background']=background[random.randint(0,2)]

            #friend['on']=models.UserProfile.objects.filter(user=user.id)[0].online
        return render(request,'friends.html',friend)

class FriendAceptView(TemplateView):
     template_name='friends.html'
     def get_context_data(self,acept,request1,request=True, **kwargs):
        context=super(FriendAceptView, self).get_context_data(**kwargs)
        to_user=models.User.objects.filter(username=context['username'])[0]
        #a=context['request']
        if request1==True:
            _from=models.User.objects.all()#(id == request.POST['reciever'])[0]
            _init_id=1
            for i in _from:
                if i.id == int(context['i_id']):
                    _init_id=i.id
            _init=models.Additive.objects.filter(id=_init_id)[0]
            models.Friend.objects.create(
                user_id_1=int(context['i_id']),
                user_id_2=to_user.id,
                joined_date=datetime.now(),
                heart1=40,
                is_friend_status=False,
                user_id1=self.request.user,#int(context['i_id']),
                user_id2=_init,
                                        )
        else:
            friend1=models.Friend.objects.filter(user_id_2=int(context['i_id']),user_id_1=to_user.id)[0]
            if acept==True:
                friend1.is_friend_status =True
                friend1.save()
                friend['friend']=[]
            else:
                friend1.delete()
            all_users=models.User.objects.all()
            for _user in all_users:
                try:
                    _user.on=models.UserProfile.objects.filter(user=_user.id)[0].online
                    _user.is_friend=True
                except (Exception):
                    pass
                friend['friend'].append(_user)
            context['friend']=friend['friend']
        return context


class FriendAddView(TemplateView):
    template_name='friends.html'
    def get_context_data(self,acept, **kwargs):
        context=super(FriendAddView, self).get_context_data(**kwargs)
        to_user=models.User.objects.filter(username=context['username'])[0]
        friend1=models.Friend.objects.filter(user_id_1=int(context['i_id']),user_id_2=to_user.id)[0]


def add_new_friend(request):
    pass



def add_new_message(request):
    '''
    db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="toshiba19",
    db='kurs_super_evm',
)
    c=db.cursor()
    c.execute('SELECT id FROM auth_user WHERE id='+request.POST['reciever'])
    entries = c.fetchall()[0]
    text=request.POST['text']
    c.execute("INSERT INTO app1_message (from_user,to_user,text, send_date,resieved_date,_from_user_id,_to_user_id) VALUES (%s,%s,%s,%s,%s,%s,%s);",
                  (request.user.pk,1,text,datetime.now(),request.user,entries))
    c.close()

    '''

    #_reciever=models.Additive.objects.filter(pk=int(request.POST['reciever']))[0].pk
    _reciever=models.User.objects.all()#(id == request.POST['reciever'])[0]
    _reciever_id=1
    for i in _reciever:
        if i.id == int(request.POST['reciever']):
            _reciever_id=i.id
    id_last=models.Additive.objects.filter(id=_reciever_id)[0]

    cache.clear()
    models.Message.objects.create(
        from_user=request.user.pk,
        to_user=id_last.id,
        text=request.POST['text'],
        send_date=datetime.now(),
        resieved_date=datetime.now(),
        _from_user=request.user,
        _to_user=id_last,
    )

    friend['friend']=[]
    all_users=models.User.objects.all()
    for _user in all_users:
        try:
            _user.on=models.UserProfile.objects.filter(user=_user.id)[0].online
        except (Exception):
                pass
        friend['friend'].append(_user)
            #friend['on']=models.UserProfile.objects.filter(user=user.id)[0].online
    sinchronize(request=request)
    return render(request,'friends.html',friend)

def add_profile(request):
    redirect_url = '/userPage/'
    if request.method == 'POST':
        form = forms.FormUserProfileEdit(request.POST)
        if form.is_valid():
            user = form.save(request)
            return HttpResponseRedirect('/userPage/')#'/autenfication/')
    else:
        form = forms.FormUserProfileEdit()
    return render(request, 'profile_edit.html', {'form': form,'continue': redirect_url})


def add_friend(request):
    pass


def add_record(request):
    redirect_url = '/userPage/'
    if request.method == 'POST':
        form = forms.FormUserWallEdit(request.POST)
        if form.is_valid():
            user = form.save(request)
            return HttpResponseRedirect('/userPage/')#'/autenfication/')
    else:
        form = forms.FormUserWallEdit()
    return render(request, 'record_add.html', {'form': form,'continue': redirect_url})

def login(request):
    redirect_url = '/'
    if request.method == 'POST':
        redirect_url = '/userPage/'
        form = forms.FormAuth(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error(None, 'invalid login/password')
    else:
        form=forms.FormAuth()
    return render(request, 'login.html', {'form':form, 'continue': redirect_url})

def register(request):
    redirect_url = '/'
    if request.method == 'POST':
        form = forms.FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            profile=models.UserProfile.objects.create(
                user=user.pk,
                photo=1,
                user_id=request.user
                                                        )
            profile.save()
            addit=models.Additive.objects.create(
                user_id=request.user
            )
            addit.save()
            return HttpResponseRedirect('/')#'/autenfication/')
    else:
        form = forms.FormRegister()
    return render(request, 'register.html', {'form': form,'continue': redirect_url})


def sinchronize(request):
    for i in models.Message.objects.all():
        all=models.UserAll.objects.filter(user_id=i.to_user)
        if len(all)==0:
            models.UserAll.objects.create(
                user_id=i.to_user,
                messages_resieved=str(i.pk)
            )
        else:
            set_of_messages=all[0].messages_resieved
            if str(i.pk) not in set_of_messages.split(','):
                all[0].messages_resieved=set_of_messages +','+str(i.pk)
                all[0].save()
        '''
        models.UserAll.objects.create(
                user_id=i.to_user,
                messages_resieved=str(i.pk)
            )

        if len(all)>0:
            all[0].message_resieved=all[0].message_resieved +','+i.pk
        '''
    #return HttpResponseRedirect('/userPage/')


def my_logout(request):
    got_offline=models.UserProfile.objects.filter(user=request.user.pk)[0]
    got_offline.online=False
    got_offline.save()
    return HttpResponseRedirect('/')




def add_message(request):
    models.Message.objects.create(
        from_user=request.user.pk,
        to_user=request.POST['reciever'],
        text=request.POST['text'],
        send_date=datetime.now(),
        resieved_date=datetime.now(),
    )
    #return render(request,'friends.html')

'''
def add_message(request):
    form=forms.MessageAdd(request.POST)
    form.save(request)
    return render(request,'friends.html')
    '''