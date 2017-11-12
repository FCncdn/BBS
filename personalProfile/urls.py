from django.conf.urls import url
from .views import personalProfileDetail, personalProfileSetting, personalProfileSettingMF

urlpatterns = [
    url(r'^mainPage/$', personalProfileDetail.as_view(), name='personalProfileMain'),
    #url(r'^settingPage/$',  personalProfileSetting, name='personalProgileSetting'),
    url(r'^settingPage/$',  personalProfileSettingMF, name='personalProgileSetting'),
]
