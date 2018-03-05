from .answers import *
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

ans_this_wk = ans_1


class MessageManager(models.Manager):
    def get_queryset(self):
        return super(MessageManager, self).get_queryset().filter(status='incoming')


class Message(models.Model):

    ANSWER_CHOICES = (
        ('ans_this_wk', 'this_week'),
        ('ans_this_wk<18', 'this_week<18'),
        ('ans_mr_this_wk', 'mr_this_week'),
        ('ans_ms_this_wk', 'ms_this_week'),
        ('ans_next_wk', 'next_week'),
        ('ans_next_wk<18', 'next_week<18'),
        ('ans_mr_next_wk', 'mr_next_week'),
        ('ans_ms_next_wk', 'ms_next_week'),
        ('inv_m_orday', 'inv_m'),
        ('inv_m_wknday', 'inv_m_wknd'),
        ('inv_f_orday', 'inv_f'),
        ('inv_f_wknday', 'inv_f_wknd'),
        ('inv_mr_orday', 'inv_mr'),
        ('inv_mr_wknday', 'inv_mr_wknd'),
        ('inv_ms_orday', 'inv_ms'),
        ('inv_ms_wknday', 'inv_ms_wknd'),

    )

    selected = models.BooleanField(default=False)
    author = models.CharField(max_length=50)
    ad_body = models.TextField()
    ad_date = models.DateTimeField(default=timezone.now)
    date_hierarchy = 'ad_date'
    answer = models.TextField(choices=ANSWER_CHOICES, default='ans_this_wk')
    status = models.CharField(max_length=10, default='incoming')
    objects = models.Manager()
    incoming = MessageManager()


class Answer(models.Model):
    s




