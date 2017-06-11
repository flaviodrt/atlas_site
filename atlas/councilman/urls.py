from django.conf.urls import url
from councilman import views
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^vereadores/(?P<slug>[\w-]+)$', views.detail, name='councilman'),
    url(r'^vereador/(?P<slug>[\w-]+)$', RedirectView.as_view(pattern_name='councilman', permanent=True)),

    url(r'^vereadores/treemap.json$', views.treemap, name='treemap')
]
