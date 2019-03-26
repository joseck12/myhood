from django import forms
from .models import Profile,Post,User,Business,hoodpro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']
        fields = ['username','profile_image','hoodpro','location']

class PostForm(forms.ModelForm):
    image_name = forms.CharField(max_length = 30)

    class Meta:
        model = Post
        fields = ['post','image','hoodpro','link','post_description']

class BusinessForm(forms.ModelForm):
    business_name = forms.CharField(max_length = 30)

    class Meta:
        model = Business
        fields = ['business_name','product','business_email']

class CommunityForm(forms.ModelForm):
    hoodpro_name= forms.CharField(max_length = 30)

    class Meta:
        model =  hoodpro
        exclude = ['user']
        