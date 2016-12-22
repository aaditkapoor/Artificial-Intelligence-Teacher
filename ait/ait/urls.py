"""ait URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from signup.views import register,login, guest_mode
from .views import home_main, get_info, feed, login_get_info,add_data, send_mails, view_data, exit_session,automatic_generation, eval_command
from marketplace.views import home,add_item, step_two_add_market, exit_session_market, install

urlpatterns = [
    url(r'^$',home_main),
    url(r'^admin/', admin.site.urls),
    url(r'^exit-session/$',exit_session),
    url(r'^send_mails/$',send_mails),
    url(r'^market_home/$',home),
    url(r'exit-session-market/$',exit_session_market),
    url(r'market_add_main/',add_item),
    url(r'^market_add_item/',add_item),
    url(r'^guest-mode/$',guest_mode),
    url(r'^command/',eval_command),
    url(r'^register/',register),
    url(r'^automatic-generation/$',automatic_generation),
    url(r'^view/$',view_data),
    url(r'^get-info-login/$',login_get_info),
    url(r'^login/',login),
    url(r'^get-info/$',get_info),
    url(r'^feed/',feed),
    url(r'add/',add_data),
    url(r'market_add_step_two/',step_two_add_market),
    url(r'^install',install),
]
