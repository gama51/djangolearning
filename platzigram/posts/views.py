from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostsForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy
from users.models import Profile
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




# def list_posts(request):
#     content=[]
#     for post in posts:
#         content.append("""
#           <p><strong>{title}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src="{photo}"/></figure>
#         """.format(**post)
#         )
#     return HttpResponse('<br>'.join(content))

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


# @login_required    
# def list_posts_ex(request):
#        profile = request.user.profile
#        posts=Post.objects.all().order_by('-created')
#        return render(
#            request=request, 
#            template_name='posts/feed.html',
#            context={
#                'posts':posts,
#                'profile':profile
#            })

# @login_required
# def create_post(request):
#    if request.method=='POST':
#        form=PostsForm(request.POST,request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')
#    else:
#        form = PostsForm()
        
#    return render (
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form':form,
#             'user':request.user,
#             'profile':request.user.profile
#         }
#     )
  
class PostFeedView(LoginRequiredMixin,ListView):
      template_name='posts/feed.html'
      model=Post
      ordering=('-created',)
      paginate_by=2
      context_object_name='posts'


class PostDetailView(LoginRequiredMixin,DetailView):
      template_name='posts/detail.html'
      queryset=Post.objects.all()
      context_object_name='post'


class CreatePostView(LoginRequiredMixin,CreateView):
    template_name='posts/new.html'
    form_class=PostsForm
    success_url=reverse_lazy('posts:feed')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context