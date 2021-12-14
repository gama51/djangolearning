from django.urls import path
from posts import views


urlpatterns=[
    
     path(
        route='post/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
        ),
    path(route='',
         view=views.PostFeedView.as_view(),
         name='feed'
         ),
    path(route='new/',
         view=views.CreatePostView.as_view(),
         name='create'
         ),        
   
]