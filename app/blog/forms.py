from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    author_name = forms.CharField(
        label="Ваше імʼя",
        required=False
    )

    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
