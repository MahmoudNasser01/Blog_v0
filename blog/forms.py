from django import forms
from blog.models import Comment, Post

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class CreatePostForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='محتوي التدوينه', widget = forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']

