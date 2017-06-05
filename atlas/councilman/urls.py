from django.conf.urls import url
from councilman import views

urlpatterns = [

    url(r'^(?P<slug>[\w-]+)$', views.detail, name='councilman'),
    url(r'^treemap.json$', views.treemap, name='treemap')
]
