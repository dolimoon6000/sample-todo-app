from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/todoitem/$', views.todo_item_list),
    url(r'^api/todoitem/(?P<pk>[0-9]+)/$', views.todo_item_detail),
]