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
#               return redirect(reverse('blog:afterlogin'))
               return HttpResponse('hello world')
            else:
               msg = 'username or password is not true!'
               return render(request,'friend/sign_in.html',{'form':form,'msg':msg})
       else:
             msg = 'the format is not correct!'
             return render(request,'friend/sign_in.html',{'form':form,'msg':msg})
def test(request):
    return HttpResponse('hello world')



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

