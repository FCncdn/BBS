from django.conf.urls import url
from .views import personalProfileDetail, personalProfileSetting, personalProfileSettingMF

urlpatterns = [
    url(r'^mainPage/$', personalProfileDetail.as_view(), name='personalProfileMain'),
    #url(r'^settingPage/$',  personalProfileSetting, name='personalProfileSetting'),
    url(r'^settingPage/$',  personalProfileSettingMF, name='personalProfileSetting'),
]
