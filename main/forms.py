from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea", "rows": '3', 'placeholder': 'Leave your comment'}))
    class Meta:
        model = Comment
        fields = ['description']