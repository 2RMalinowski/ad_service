from answers import ans_1
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
ans_this_wk = ans_1


class Message(models.Model):

    ANSWER_CHOICES = (
        ('ans_this_wk', 'this_week'),
        ('ans_this_wk<18', 'this_week<18'),
        ('ans_ms_this_wk', 'ms_this_week'),
        ('ans_mr_this_wk', 'mr_this_week'),
        ('ans_next_wk', 'next_week'),
        ('ans_next_wk<18', 'next_week<18'),
        ('ans_ms_next_wk', 'ms_next_week'),
        ('ans_mr_next_wk', 'mr_next_week'),
    )
    
    selected = models.BooleanField(default=False)
    author = models.CharField(max_length=50)
    ad_body = models.TextField()
    ad_date = models.DateTimeField(default=timezone.now)
    answer = models.TextField(choices=ANSWER_CHOICES, default='ans_this_wk')
