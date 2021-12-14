from django import forms
from django.db.models.fields import NullBooleanField
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from users.models import Profile
from django.db.utils import IntegrityError
from users.form import ProfileForm,SignUpForm
from django.views.generic import DetailView, UpdateView
from django.urls import reverse
from posts.models import Post
# Create your views h
# ere.

# def login_view(request):
#     if request.method=='POST':
#        username=request.POST['username']
#        password=request.POST['password']
#        user=authenticate(request,username=username,password=password)
#        if user:
#            login(request,user)
#            return redirect('posts:feed')
#        else:
#            return render(request,'users/login.html',{'error':'Ivalid user or password'})         
#     return render(request,'users/login.html')

class LoginView(auth_views.LoginView):
      template_name='users/login.html'

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name='users/logged_out.html'
    
      

# def signup_view(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         password_confirmation=request.POST['password_confirmation']
#         if password!=password_confirmation:
#             return render(request,'users/signup.html',{'error':'Password confirmation does not match'})
#         try:    
#             user=User.objects.create_user(username=username,password=password)    
#         except IntegrityError:
#             return render(request,'users/signup.html',{'error':'user name is allready in use'})

#         user.first_name=request.POST['first_name']
#         user.last_name=request.POST['last_name']
#         user.email=request.POST['email']
#         user.save()
#         profile = Profile(user=user)
#         profile.save()
#         return redirect('login')

# def signup_view(request):
#     if request.method == 'POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form=SignUpForm()
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={
#             'form':form,            
#         }

#     )

class SignUpVieW(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

   
# @login_required
# def update_profile(request):
#     profile = request.user.profile
#     if request.method=='POST':
#         form=ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             data=form.cleaned_data
#             profile.website=data['website']
#             profile.phone_number=data['phone_number']
#             profile.biography=data['biography']
#             profile.picture =data['picture']
#             profile.save()
#             url=reverse('users:detail',kwargs={'username':request.user.username})
#             return redirect(url)
#     else:
#         form=ProfileForm()    
#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,

#             'form':form
#         }
#     )
class UpdateProfileView(LoginRequiredMixin,UpdateView):
      template_name='users/update_profile.html'
      model=Profile
      fields=[
          'website',
          'biography',
          'phone_number',
          'picture'
      ]


      def get_object(self):
          return self.request.user.profile
       

      def get_success_url(self):
           username=self.object.user.username
           return reverse('users:detail',kwargs={'username':username})

class UserDetailView(LoginRequiredMixin,DetailView):
      
      
      template_name='users/detail.html'
      slug_field='username'
      slug_url_kwarg='username'
      queryset=User.objects.all()
      context_object_name='user'

      def get_context_data(self,**kwargs):
          context=super().get_context_data(**kwargs)
          user=self.get_object()
          context['posts']=Post.objects.filter(user=user).order_by('-created')
          return context


