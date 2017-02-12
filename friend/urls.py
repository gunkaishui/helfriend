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
     url(r'^friadd$',friend_add,name='friend_add'),
     url(r'^logout$',log_out,name='logout'),

     url(r'^quxiao$',quxiao,name='quxiao'),
     url(r'^testtwo$',testtwo,name='testtwo'),
     url(r'^seting$',seting,name='seting'),
     url(r'^alter$',seting_alter,name='seting_alter'),
     url(r'^history/(?P<user_id>[0-9]+)$',history,name='history'),


]
