from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import blog_post
class registerForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    image=forms.ImageField(required=False)
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'image',
         
        ]

class update_profile(UserChangeForm):
            password=None
            class Meta:
                model=User
                fields=[
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    
                
                ]

class post_form(forms.ModelForm):
      class Meta:
            model=blog_post
            exclude=['author',] 
            widgets={
                  'title':forms.TextInput(attrs={'placeholder':'Write Post Title..'}),
                  'content':forms.Textarea(attrs={'rows':3,'placeholder':'Write your content here...'})
                  
            }