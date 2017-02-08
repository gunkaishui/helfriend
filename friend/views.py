from django.shortcuts import render

# Create your views here.

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
    return render(request,'friend/fabiao.html')



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
                   return redirect(reverse('friend:test'))
            else:
                msg = 'the username is already exist!'
                return render(request,'friend/sign_up.html',{'form':form,'msg':    msg})
         else:
             msg = 'format is not correct!'
             return render(request,'friend/sign_up.html',{'form':form,'msg':msg    })

def after_login(request):
    this_user = request.user
    fri_id_char = this_user.friends_id
    fri_id_list = fri_id_char.split(',')
    affair_set = this_user.affair_set.order_by('-pub_date')
    for fri_id in fri_id_list:
        affair_set = affair_set | FriUser.objects.get(id=int(fri_id)).affair_set.order_by('-pub_date')
    affair_set = affair_set.order_by('-pub_date')
    dictionary = {'affair_set':affair_set}
    return render(request,'friend/main.html',dictionary)

def sub_affair(request):
    if request.method == 'POST':
        newaffair = Affair()
        newaffair.author = request.user
        newaffair.content = request.POST['affair_sub']
        newaffair.save()
        return redirect(reverse('friend:afterlogin'))
    else:
        return render(request,'friend/fabiao.html')
