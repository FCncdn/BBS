from django.conf import settings
from django.conf.urls import url
if getattr(settings, 'POSTMAN_I18N_URLS', False):
    from django.utils.translation import pgettext_lazy
else:
    def pgettext_lazy(c, m): return m
from django.views.generic.base import RedirectView

from postman.views import (InboxView, SentView, ArchivesView, TrashView,
        WriteView, ReplyView, MessageView, ConversationView,
        ArchiveView, DeleteView, UndeleteView, MarkReadView, MarkUnreadView)
from .moderation import mod1, mod2

urlpatterns = [
    url(r'^write/(?:(?P<recipients>[^/#]+)/)?$',
        WriteView.as_view(auto_moderators=mod1),
        name='write'),
    url(r'^reply/(?P<message_id>[\d]+)/$',
        ReplyView.as_view(auto_moderators=mod2),
        name='reply'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^inbox/(?:(?P<option>m)/)?$'), InboxView.as_view(), name='inbox'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^sent/(?:(?P<option>m)/)?$'), SentView.as_view(), name='sent'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^archives/(?:(?P<option>m)/)?$'), ArchivesView.as_view(), name='archives'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    url(pgettext_lazy('postman_url', r'^trash/(?:(?P<option>m)/)?$'), TrashView.as_view(), name='trash'),
    #url(pgettext_lazy('postman_url', r'^write/(?:(?P<recipients>[^/#]+)/)?$'), WriteView.as_view(), name='write'),
    #url(pgettext_lazy('postman_url', r'^reply/(?P<message_id>[\d]+)/$'), ReplyView.as_view(), name='reply'),
    url(pgettext_lazy('postman_url', r'^view/(?P<message_id>[\d]+)/$'), MessageView.as_view(), name='view'),
    # Translators: 't' stands for 'thread'
    url(pgettext_lazy('postman_url', r'^view/t/(?P<thread_id>[\d]+)/$'), ConversationView.as_view(), name='view_conversation'),
    url(pgettext_lazy('postman_url', r'^archive/$'), ArchiveView.as_view(), name='archive'),
    url(pgettext_lazy('postman_url', r'^delete/$'), DeleteView.as_view(), name='delete'),
    url(pgettext_lazy('postman_url', r'^undelete/$'), UndeleteView.as_view(), name='undelete'),
    url(pgettext_lazy('postman_url', r'^mark-read/$'), MarkReadView.as_view(), name='mark-read'),
    url(pgettext_lazy('postman_url', r'^mark-unread/$'), MarkUnreadView.as_view(), name='mark-unread'),
    url(r'^$', RedirectView.as_view(url='inbox/', permanent=True)),
]