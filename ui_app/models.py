from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    ANSWER_CHOICES = (
        ('ans_this_week', 'twk'),
        ('ans_this_week_u18', 'twu18'),
        ('ans_ms_this_week', 'mstwk'),
        ('ans_mr_this_week', 'mrtwk'),
        ('ans_next_week', 'nwk'),
        ('ans_next_week_u18', 'nwu18'),
        ('ans_ms_next_week', 'msnwk'),
        ('ans_mr_next_week', 'mrnwk'),
    )
    selected = models.BooleanField(default=False)
    author = models.CharField(max_length=50)
    ad_body = models.TextField()
    ad_date = models.DateTimeField(default=timezone.now)
