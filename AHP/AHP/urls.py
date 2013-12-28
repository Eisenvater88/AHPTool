from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from AHPTool import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AHP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^save/', views.save, name = 'save'),
    url(r'^result/', views.generateResult, name = 'generateResult'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': 'C:/Users/Sobiech/workspace/AHP/AHPTool/Templates/AHPTool'}),
)
