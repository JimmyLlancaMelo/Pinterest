from django.views.generic import View
from django.shortcuts import render, redirect, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social.forms import SocialPostForm, SharedForm
from social.models import Image, SocialPost

class HomeView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        logged_in_user=request.user
        form = SocialPostForm() # Solo vemos el formulario
        posts = SocialPost.objects.all()
        share_form = SharedForm()
        context={
            'form':form,
            'posts':posts,
            'share_form':share_form
        }
        return render(request, 'pages/index.html', context)
    
    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        form = SocialPostForm(request.POST)
        share_form = SharedForm()
        if form.is_valid():
            
            new_post = form.save(commit=False) # Guarda el SocialPost sin la imagen todavía
            new_post.author = logged_in_user
            new_post.save() # Guarda el post primero
            
            image_file = request.FILES.get('image') # Obtener el archivo de imagen desde el formulario
            
            if image_file:
                img = Image(image=image_file) # Crear una nueva instancia de Image
                img.save()  # Guarda la imagen en la base de datos
                
                new_post.image = img # Asignar la instancia de Image al post
                new_post.save()  # Guarda el post nuevamente con la imagen asociada
                

        context = {
            'form':form,
            'share_form':share_form
        }
        
        return render(request,'pages/index.html',context)