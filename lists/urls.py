from django.urls import path
from . import views


urlpatterns=[
    path("",views.dashboard,name='dashboard'),
    path("list/<str:pk>",views.list, name='list'),
    path("create-list",views.createList, name='create-list'),
    path("delete-list/<str:pk>",views.deleteList, name='delete-list'),
    path("share-list/<str:pk>",views.shareList, name='share-list'),
    path("delete-task/<str:pk>",views.deleteTask,name='delete-task'),
]