from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#from friend.forms import *
from django.http import HttpResponse ,HttpResponseRedirect

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
               return render(request,'blog/index.html',{'form':form,'msg':msg})
       else:
             msg = 'the format is not correct!'
             return render(request,'blog/index.html',{'form':form,'msg':msg})
def login(request):
    return HttpResponse('hello world')
