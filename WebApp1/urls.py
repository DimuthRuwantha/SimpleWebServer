from django.conf.urls import url,include
from . import views

app_name = 'WebApp1'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),   # index is the function call in views.py
    # url(r'^fault/$', views.Fault.as_view(), name='fault'),   # index is the function call in views.py
    # url(r'^no_model/$', views.NoModel.no_model()),   # index is the function call in views.py
]
