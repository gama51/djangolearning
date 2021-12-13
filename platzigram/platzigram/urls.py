"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from platzigram.views import views as localviews
from posts import views as posts_viwes
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/',localviews.hello_world, name="hello_world"),
    path('sorted/',localviews.sorted ,name="sorted"),
    path('say_hi/<str:name>/<int:age>',localviews.say_hi,name="hi"),
    path('posts/',posts_viwes.list_posts,name="posts"),
    path('posts-ex/',posts_viwes.list_posts_ex,name="feed"),
    path('users/login/',users_views.login_view, name='login'),
    path('users/logout/',users_views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

