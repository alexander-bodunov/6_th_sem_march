__author__ = 'Work'
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userPage/0/0/0/',views.add_new_message,name="add_message"),
    url(r'^autenfication/$',views.login,name="autenfication_url"),
    url(r'^register/$',views.register,name="register_url"),
    url(r'^sinchronize/$',views.sinchronize,name="sinchonize"),
    url(r'^userPage/only_friends/$',views.FriendsOnlyView.as_view(),name='friends_only_url'),
    url(r'^userPage/profile/$',views.add_profile,name="profile_add_url"),
    url(r'^userPage/record/$',views.add_record,name="record_add_url"),
    url(r'^userPage/message/$',views.MessagesView.as_view(),name="message_url"),
    url(r'^userPage/friends/$',views.FriendsView.as_view(),name="friends_url"),
    url(r'^userPage/acept_friends/(?P<i_id>\d+)/(?P<username>\w+)$',views.FriendAceptView.as_view() ,{'acept':True,'request1':False},name="acept_url"),
    url(r'^userPage/decline_friends/(?P<i_id>\d+)/(?P<username>\w+)$',views.FriendAceptView.as_view() ,{'acept':False,'request1':False},name="decline_url"),
    url(r'^userPage/request_friends/(?P<i_id>\d+)/(?P<username>\w+)$',views.FriendAceptView.as_view() ,{'acept':False,'request1':True},name="request_url"),
    url(r'^userPage/$',views.UserView.as_view(),name="user_page_url"),
    url(r'^logout/$',views.my_logout,name="logout_url"),
    url(r'^$',views.IndexView.as_view(),name="index"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



