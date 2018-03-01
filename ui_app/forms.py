from django import forms


class MessagePostForm(forms.Form):
    author = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

