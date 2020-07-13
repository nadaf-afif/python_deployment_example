from django.conf.urls import url
from admin_user_example import views

app_name = 'admin_user'

urlpatterns = [
    url(r'^$', views.register, name="register"),
    url(r'^user_login/$', views.user_login, name="user_login")    
]



