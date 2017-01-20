from django.conf.urls import url
from friend.views import *

urlpatterns = [
     url(r'^$',sign_in,name='sign_in'),
     url(r'^login/$',login,name='login'),


]
