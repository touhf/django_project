from .models import Comment, Image
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

