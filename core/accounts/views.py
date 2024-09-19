from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import EditProfileForm

User = get_user_model() # Aqui se encuentra el usuario

class UserProfileView(View):
    
    def get(self,request, username,*args,**kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        context={
            'user':user,
            'profile':profile,
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