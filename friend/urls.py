from django.conf.urls import url
from friend.views import *

urlpatterns = [
    # url(r'^$',sign_in,name='sign_in'),
     url(r'^$',log_in,name='login'),
     url(r'^test$',test,name='test'),
     url(r'^signup$',register,name='signup'),
     url(r'^index$',after_login,name='afterlogin'),
     url(r'^subaff$',sub_affair,name='subaffair'),
     url(r'^addfri$',add_friend,name='add_friend'),
     url(r'^friend$',friend_add,name='friend_add'),

     url(r'^quxiao$',quxiao,name='quxiao'),
     url(r'^testtwo$',testtwo,name='testtwo'),


]
