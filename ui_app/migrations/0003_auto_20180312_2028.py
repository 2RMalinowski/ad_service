# Generated by Django 2.0.3 on 2018-03-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_app', '0002_remove_answer_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='ad_body',
            new_name='msg_body',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='ad_date',
            new_name='msg_date',
        ),
        migrations.AddField(
            model_name='message',
            name='ans_choice',
            field=models.TextField(choices=[('ans_this_wk', 'this_week'), ('ans_this_wk<18', 'this_week<18'), ('ans_mr_this_wk', 'mr_this_week'), ('ans_ms_this_wk', 'ms_this_week'), ('ans_next_wk', 'next_week'), ('ans_next_wk<18', 'next_week<18'), ('ans_mr_next_wk', 'mr_next_week'), ('ans_ms_next_wk', 'ms_next_week'), ('ans_other_term', 'other_term'), ('ans_other_term_mr', 'mr_other_term'), ('ans_other_term_ms', 'ms_other_term'), ('ans_office', 'office'), ('inv_m_orday', 'inv_m'), ('inv_m_wknday', 'inv_m_wknd'), ('inv_f_orday', 'inv_f'), ('inv_f_wknday', 'inv_f_wknd'), ('inv_mr_orday', 'inv_mr'), ('inv_mr_wknday', 'inv_mr_wknd'), ('inv_ms_orday', 'inv_ms'), ('inv_ms_wknday', 'inv_ms_wknd'), ('inv_scnd', 'inv_rptd'), ('inv_mr_scnd', 'inv_mr_rptd'), ('inv_ms_scnd', 'inv_ms_rptd'), ('ans_blank', 'manual')], default='ans_this_wk'),
        ),
        migrations.AlterField(
            model_name='message',
            name='answer',
            field=models.TextField(),
        ),
    ]