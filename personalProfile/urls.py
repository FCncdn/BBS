from django.conf.urls import url
from .views import personalProfileDetail, personalProfileSetting, personalProfileSettingMF
from .views import personalProfileDynamic
from .views import personalProfileFavourite

urlpatterns = [
    url(r'^mainPage/$', personalProfileDetail.as_view(), name='personalProfileMain'),
    url(r'^settingPage/$', personalProfileSettingMF, name='personalProfileSetting'),
    url(r'^dynamicPage/$', personalProfileDynamic, name='personalProfileDynamic'),
    url(r'^favouritePage/$', personalProfileFavourite, name='personalProfileFavourite'),
]
