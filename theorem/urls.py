from django.conf.urls import url
from . import views

app_name = 'theorem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get-url-details/$', views.get_url_details, name='get_url_details')
]