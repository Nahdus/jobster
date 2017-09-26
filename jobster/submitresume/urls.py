

from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name='submitresume'
urlpatterns = [
    url(r'^register$',views.userformview.as_view(), name ='register'),
    url(r'^login/$',views.login_user,name='login' ),
    url(r'^$',views.resume_form.as_view(), name ='submit-resume'),
    url(r'^index/(?P<resume_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^selected/(?P<resume_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^index/(?P<resume_id>[0-9]+)/select/$', views.select_resume, name='select'),
    url(r'^selected/$', views.selected_list, name='selected_list'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^index/$', views.index, name='index'),


]