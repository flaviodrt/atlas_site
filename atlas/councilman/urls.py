from django.conf.urls import url
from councilman import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vereador/(?P<slug>[\w-]+)$', views.show, name='councilman'),

]
