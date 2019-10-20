from django import forms

from .models import Post,Update

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('customername', 'amount',)

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update
        fields = ( 'givenamount',)