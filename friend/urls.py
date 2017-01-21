from django.conf.urls import url
from friend.views import *

urlpatterns = [
    # url(r'^$',sign_in,name='sign_in'),
     url(r'^$',log_in,name='login'),
     url(r'^test$',test,name='test'),
     url(r'^signup$',register,name='signup'),


]
