from django.conf.urls import url
from councilman import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
