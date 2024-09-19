from .models import Profile
from django import forms

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))  # Para archivos
    banner = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))  # Para archivos
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))  # Para textos largos
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))  # Input de tipo 'date'
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'banner', 'location', 'url', 'bio', 'birthday')
