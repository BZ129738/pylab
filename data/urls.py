from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.data),
    url(r'^page', views.page),
    url(r'^myname', views.myname)
]