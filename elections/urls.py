from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^polls/(?P<poll_id>\d+)/$', views.polls)
    url(r'^polls/$', views.polls),
    #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
    url(r'^game/$', views.game)
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


