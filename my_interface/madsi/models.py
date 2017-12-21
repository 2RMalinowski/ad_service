from django.db import models


class Message(models.Model):
    content = models.CharField(max_length=500)
    email = models.TextField(max_length=64)



ANSWER_CHOICES = (
    ('ans_this_wk', 'twk'),
    ('ans_this_wk_u18', 'twu18'),
    ('ans_ms_this_wk', 'mstwk'),
    ('ans_mr_this_wk', 'mstwk'),
    ('ans_next_wk', 'twk'),
    ('ans_next_wk_u18', 'twu18'),
    ('ans_ms_next_wk', 'msnwk'),
    ('ans_mr_next_wk', 'mrnwk'),

)


class MyAnswer(models.Model):
    answer = models.CharField(max_length=500, )
