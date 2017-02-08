# -*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect,get_object_or_404

from django.core.exceptions import ObjectDoesNotExist

from friend.forms import *
from django.http import HttpResponse ,HttpResponseRedirect
from friend.models import *
def sign_in(request):
    return render(request,'friend/sign_in.html')

def log_in(request):
    if request.method == 'GET':
       form = LoginForm()
       return render(request,'friend/sign_in.html',{'form':form})
    else:
       form = LoginForm(request.POST)
       if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username,password=password)
            if user  and user.is_active:
               login(request,user)
               return redirect(reverse('friend:afterlogin'))
            else:
               msg = 'username or password is not true!'
               return render(request,'friend/sign_in.html',{'form':form,'msg':msg})
       else:
             msg = 'the format is not correct!'
             return render(request,'friend/sign_in.html',{'form':form,'msg':msg})
def test(request):
    return render(request,'friend/friend_add.html')



def register(request):
      if request.method == 'GET':
         form = RegisterForm()
         return render(request,'friend/sign_up.html',{'form':form})
      else:
         form = RegisterForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            try:
               user =  FriUser.objects.get(username=username)
            except ObjectDoesNotExist:
               if password1 != password2:
                  msg = 'two password is not same!'
                  return render(request,'friend/sign_up.html',{'form':form,'msg':msg})
               else:
                   newuser = FriUser()
                   newuser.username = username
                   newuser.set_password(password1)
                   newuser.save()
                   login(request,newuser)
                   return redirect(reverse('friend:afterlogin'))
            else:
                msg = 'the username is already exist!'
                return render(request,'friend/sign_up.html',{'form':form,'msg':    msg})
         else:
             msg = 'format is not correct!'
             return render(request,'friend/sign_up.html',{'form':form,'msg':msg    })

def after_login(request):
        add_id_list = str_to_list(request.user.add_fri_id)
        try:
             add_id_list.remove('')
        except:
               pass
        if add_id_list is None:
            affair_set = request.user.affair_set.order_by('-pub_date')
            fri_id_list = str_to_list(request.user.friends_id)
            try:
                fri_id_list.remove('')
            except:
                pass
            if fri_id_list is not None:
                for fri_id in fri_id_list:
                    affair_set = affair_set | FriUser.objects.get(id=int(fri_id)).affair_set.order_by('-pub_date')
            affair_set = affair_set.order_by('-pub_date')
            dictionary = {'affair_set':affair_set}
            return render(request,'friend/main.html',dictionary)
        else:
               userlist = []
               for i in add_id_list:
                    user = FriUser.objects.get(id=int(i))
                    userlist.append(user)
               return render(request,'friend/friend_add.html',
                            {'userlist':userlist})                 
                    
def sub_affair(request):
    if request.method == 'POST':
        newaffair = Affair()
        newaffair.author = request.user
        newaffair.content = request.POST['affair_sub']
        newaffair.save()
        return redirect(reverse('friend:afterlogin'))
    else:
        return render(request,'friend/fabiao.html')

def add_friend(request):
        if request.method == 'GET':
             return render(request,'friend/add_friend.html')
        else:
            try: 
                  this_user = request.user
                  that_user = FriUser.objects.get(username=request.POST['username'])
                  friend_id_list = str_to_list(this_user.friends_id)
                  if (friend_id_list is  None) or(str(that_user.id) not in                         friend_id_list) :
                      
                       add_fri_id_list = str_to_list(that_user.add_fri_id)
                       if add_fri_id_list is not None:
                       
                           add_fri_id_list.append(str(this_user.id))
                           that_user.add_fri_id = ','.join(set(add_fri_id_list))
                       else:
                           that_user.add_fri_id = str(this_user.id)

                       that_user.save()
                       return redirect(reverse('friend:afterlogin'))
                  else:
                       msg = '该用户已经是您的好友'
                       return render(request,'friend/add_friend.html',{'msg':msg})
            except:
                  msg = '该用户不存在'
                  return render(request,'friend/add_friend.html',{'msg':msg})

                        
def quxiao(request):
    return redirect(reverse('friend:afterlogin'))


def str_to_list(string):
        if string is None:
               return None
        else:
               return string.split(',')
       
def testtwo(request):
     receive = request.POST.getlist('vehicle')
     return HttpResponse(receive[1])

def  friend_add(request):
      userids = request.GET.getlist('username') 
      friends_id_list = str_to_list(request.user.friends_id)
      if friends_id_list is None:
           friends_id_list = userids
      else:
          friends_id_list = friends_id_list + userids
      request.user.friends_id = ','.join(set(friends_id_list))
      request.user.add_fri_id = None
      request.user.save()
      for i in userids:
             user = FriUser.objects.get(id=int(i))
             idlist = str_to_list(user.friends_id)
             if idlist is None:
                  user.friends_id = i
             else:
                  idlist.append(str(request.user.id))
                  user.friends_id = ','.join(set(idlist))
             user.save()           
      return redirect(reverse('friend:afterlogin'))
