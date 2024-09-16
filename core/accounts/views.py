from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model
from accounts.models import Profile

User = get_user_model() # Aqui se encuentra el usuario

class UserProfileView(View):
    def get(self,request, username,*args,**kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        context={
            'user':user,
            'profile':profile
        }
        return render(request,'pages/users/detail.html', context)
