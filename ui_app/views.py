<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, get_object_or_404
from .models import Answer, Message


def message_list(request):
    return render(request, 'ui_app/message_list.html', {})


def answer_list(request):
    return render(request, 'ui_app/answer_list.html', {})

>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
