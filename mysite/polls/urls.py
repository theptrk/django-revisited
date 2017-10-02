from django.conf.urls import url

from . import views

# use the app_name to namespace a url
# so instead of  {% url 'detail' %} in the template we would now use
# {% url polls:detail %}
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]