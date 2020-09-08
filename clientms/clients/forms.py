from django import forms
from .models import Comment
from django.forms import ModelForm

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['client', 'comment']

