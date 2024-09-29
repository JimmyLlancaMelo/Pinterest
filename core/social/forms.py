from django import forms
from .models import SocialPost, SocialComment

class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=True)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False) # Django en su ultima version no soporta la carga de multiples imagenes y por ende bota error
    
    class Meta:
        model=SocialPost
        fields=['body','image']

class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=True)
    
    class Meta:
        model=SocialComment
        fields=['comment']