from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from bbs import views
from personalProfile.views import MySearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article),
    url(r'^partition/(?P<category_id>[0-9]+)/(?P<page>[0-9]+)/$', views.partition, name='partition'),
    #url(r'^article_post/', views.article_post),
    url(r'^sub_page/', views.sub_page),
    url(r'^login/$', views.login),
    url(r'^acc_login/$', views.acc_login),
    url(r'^logout/$', views.logout_view),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^sub_article/$', views.sub_article),
    url(r'^register/$', views.register_handle, name='register')
]

#custom app
#personalProfile
#**********WARNING**********
#Use User's id and don't use UserProfile's id in template and views
#**********WARNING**********
urlpatterns += [
    url(r'^profile/(?P<pk>[0-9]+)/',
        include('personalProfile.urls', namespace='personalProfile', app_name='personalProfile')),
]

#backend system
urlpatterns += [
    url(r'^backendSys/(?P<pk>[0-9]+)/',
        include('backendSys.urls', namespace='backendSys', app_name='backendSys')),
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

#message - hostman
urlpatterns += [
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
]