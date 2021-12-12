from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from posts.models import Post


# Register your models here.
@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','title','user','profile')
    list_display_links=('title','user')
    search_fields=('post__title','post__user.name')
    list_filter=('created','modified')