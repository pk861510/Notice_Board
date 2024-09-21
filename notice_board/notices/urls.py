from django.urls import path
from . import views

urlpatterns = [
    path('',views.notice_list, name='notice_list'),  #homepage for listing notice
    path('new/',views.create_notice, name='create-notice'), # page for creating new notice
]