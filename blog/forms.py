from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ['post']
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "text": "Your Feedback",
            "rating": "Your Rating"
        }