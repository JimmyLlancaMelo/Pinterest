from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

User = get_user_model() # Aqui se encuentra el usuario

class UserProfileView(View):
    
    def get(self,request, username,*args,**kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        followers = profile.followers.all()
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
        if len(followers) == 0:
            is_following=False
        
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            
            else:
                is_following = False
        
        numbers_of_followers = len(followers)
        
        context={
            'user':user,
            'profile':profile,
            'follower':followers,
            'number_followers':numbers_of_followers,
            'is_following':is_following
        }
        return render(request,'pages/users/detail.html', context)

    def post(self,request,*args,**kwargs):
        user = request.user.id # el request es el nombre del usuario que esta con login
        profile = Profile.objects.get(user__id=user)

        user_basic_info = User.objects.get(id=user)
        
        if request.method == 'POST':
            form=EditProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                user_basic_info.first_name = form.cleaned_data.get('first_name')
                user_basic_info.last_name = form.cleaned_data.get('last_name')
                profile.picture = form.cleaned_data.get('picture')
                profile.banner = form.cleaned_data.get('banner')
                profile.location = form.cleaned_data.get('location')
                profile.url = form.cleaned_data.get('url')
                profile.birthday = form.cleaned_data.get('birthday')
                profile.bio = form.cleaned_data.get('bio')
                
                profile.save()
                user_basic_info.save()
                
                return redirect('users:profile', request.user.username)
        else:
            form = EditProfileForm(instance=profile)
        context={
            'form':form
        }
        return render(request, 'pages/users/edit.html', context)

class AddFollower(LoginRequiredMixin, View):
    def post(self, request,pk, *args,**kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)
        messages.add_message(self.request, messages.SUCCESS,'User Followed')
        return redirect('users:profile', username=request.user.username)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request,pk, *args,**kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        messages.add_message(self.request, messages.SUCCESS,'User Unfollowed')
        return redirect('users:profile', username=request.user.username)

class ListFollower(View):
    def get(self,request,pk,*args,**kwargs):
        profile = Profile.objects.get(pk=pk)
        followers = profile.followers.all()
        context={
            'profile':profile,
            'followers':followers,
        }
        return render(request, 'pages/social/followers-list.html',context)