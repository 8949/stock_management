# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IteamsList.as_view(), name='Iteams_list'),
    path('view/<int:pk>', views.IteamsDetail.as_view(), name='Iteams_view'),
    path('new', views.create_iteam , name='Iteams_new'),
    # path('new', views.IteamsCreate.as_view(), name='Iteams_new'),
    path('edit/<int:pk>', views.IteamsUpdate.as_view(), name='Iteams_edit'),
    path('delete/<int:pk>', views.IteamsDelete.as_view(), name='Iteams_delete'),
]
