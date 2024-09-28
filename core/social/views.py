from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import View
from .models import SocialPost
from django.views.generic.edit import UpdateView, DeleteView

class PostDetailView(LoginRequiredMixin,View):
    
    def get(self,request,pk, *args,**kwargs):
        post = SocialPost.objects.get(pk=pk)
        context={
            'post':post
        }
        return render(request, 'pages/social/detail.html', context)
    def post(self,request,pk, *args,**kwargs):
        post = SocialPost.objects.get(pk=pk)
        context={
            'post':post
        }
        return render(request, 'pages/social/detail.html', context)


class PostEditView(UserPassesTestMixin, UpdateView):
    model=SocialPost
    fields=['body']
    template_name='pages/social/edit.html'
     
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model=SocialPost
    template_name='pages/social/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class AddLike(LoginRequiredMixin, View):
    def post(self,request,pk, *args,**kwargs):
        post = SocialPost.objects.get(pk=pk)

        is_dislike=False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike=True
                break
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like=False
        for like in post.likes.all():
            if like == request.user:
                is_like=True
                break
        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)
        
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self,request,pk, *args,**kwargs):
        post = SocialPost.objects.get(pk=pk)

        is_like=False
        for like in post.dislikes.all():
            if like == request.user:
                is_like=True
                break
        if is_like:
            post.dislikes.remove(request.user)

        is_dislike=False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike=True
                break
        if not is_dislike:
            post.dislikes.add(request.user)
        if is_like:
            post.dislikes.remove(request.user)
        
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)