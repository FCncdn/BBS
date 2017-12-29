"""BBSPRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.conf.urls import url,include
from django.contrib import admin
from bbs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article),
    url(r'^partition/(?P<category_id>[0-9]+)/(?P<page>[0-9]+)/$', views.partition, name='partition'),
    url(r'^article_post/', views.article_post),
    url(r'^login/$', views.login),
    url(r'^acc_login/$', views.acc_login),
    url(r'^logout/$', views.logout_view),

]

#custom app
#personalProfile
urlpatterns += [
    url(r'^profile/(?P<pk>[0-9]+)/',
        include('personalProfile.urls', namespace='personalProfile', app_name='personalProfile')),
]

#for upload file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#third-party app
#debug_tool_bar - only work on development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

#serch 
urlpatterns += [
    url(r'^search/', include('haystack.urls')),
]
