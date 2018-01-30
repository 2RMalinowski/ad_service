from django import forms


class MessageForm(forms.Form):
    content = models.TextField()
    email = models.CharField(max_length=64)
