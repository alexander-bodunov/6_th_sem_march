from django.db import models
from django.contrib.auth.models import User,BaseUserManager, AbstractUser
# Create your models here.


'''
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    online=models.BooleanField(default=False)
'''

class UserAll(models.Model):
    user_id=models.IntegerField()
    messages_send=models.TextField(null=True,blank=True)
    messages_resieved=models.TextField(null=True,blank=True)
    #friends=models.TextField(null=True,blank=True)



class UserProfile(models.Model):
    online=models.BooleanField(default=False)
    user=models.IntegerField(null=True);
    #photo=models.ImageField(null=True,blank=True);
    photo=models.IntegerField(max_length=100);
    user_id=models.ForeignKey(User,related_name='+')


class Wall(models.Model):
    title=models.TextField(max_length=40);
    text=models.TextField(max_length=400);
    posted=models.DateTimeField();
    is_commentable=models.BooleanField();
    my_user=models.IntegerField()#ManyToManyField(UserProfile, related_name='wall_posts',blank=True,null=True);
    user_id=models.ForeignKey(User,related_name='+')


class Additive(models.Model):
    user_id=models.ForeignKey(User,related_name='user_id',null=True,blank=True)



class Message(models.Model):
    from_user=models.IntegerField()
    to_user=models.IntegerField()
    text=models.TextField()
    send_date=models.DateTimeField()
    resieved_date=models.DateTimeField(null=True,blank=True)
    _from_user=models.ForeignKey(User,related_name='+')
    _to_user=models.ForeignKey(Additive,related_name='+',null=True,blank=True)




class Friend(models.Model):
    user_id_1=models.IntegerField(null=True,blank=True)
    user_id_2=models.IntegerField(null=True,blank=True)
    joined_date=models.DateTimeField()
    heart1=models.IntegerField(null=True,blank=True)
    heart2=models.IntegerField(null=True,blank=True)
    is_friend_status=models.BooleanField()
    user_id1=models.ForeignKey(User,related_name='+')
    user_id2=models.ForeignKey(Additive,related_name='+')

class Like(models.Model):
    post_id=models.ForeignKey(Wall)
    user_id=models.ForeignKey(User,related_name='+')
    is_like=models.BooleanField

class NotesAboutUser(models.Model):
    user_id=models.ForeignKey(User,related_name='+')
    description=models.TextField()
    date=models.DateTimeField()

class Design(models.Model):
    user_id=models.ForeignKey(User,related_name='+')
    photo_baground_class=models.FileField()
    photo_friend_class=models.FileField()
    photo_message_class=models.FileField()
    music=models.FileField(upload_to='/audio/')









