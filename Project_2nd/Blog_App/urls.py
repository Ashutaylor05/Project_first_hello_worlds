from django.urls import path
from .views import  BlogListView,BlogDetails
from . import views
urlpatterns=[

    path('blogs',BlogListView.as_view(),name="list_blog"),
    # path('post/<int:pk>/', BlogDetails.as_view(), name='detail'),
    path('post/<int:id>', views.BlogDetails, name='detail'),
 # new

]