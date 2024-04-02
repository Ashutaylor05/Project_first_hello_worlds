from django.urls import path
from .views import List_msg

urlpatterns = [
    path('List_msg', List_msg.as_view(), name='list msg'),
]