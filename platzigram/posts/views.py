from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostsForm
from django.shortcuts import redirect
# Create your views here.

# posts = [
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/600?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/500/700/?image=1076',
#     }
# ]




def list_posts(request):
    content=[]
    for post in posts:
        content.append("""
          <p><strong>{title}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{photo}"/></figure>
        """.format(**post)
        )
    return HttpResponse('<br>'.join(content))

# @login_required    
# def list_posts_ex(request):
#        profile = request.user.profile
#        return render(
#            request=request, 
#            template_name='posts/feed.html',
#            context={
#                'posts':posts,
#                'profile':profile
#            }) 


@login_required    
def list_posts_ex(request):
       profile = request.user.profile
       posts=Post.objects.all().order_by('-created')
       return render(
           request=request, 
           template_name='posts/feed.html',
           context={
               'posts':posts,
               'profile':profile
           })

@login_required
def create_post(request):
   if request.method=='POST':
       form=PostsForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('feed')
   else:
       form = PostsForm()
        
   return render (
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile':request.user.profile
        }
    )
  
