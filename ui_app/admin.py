from django.contrib import admin
from .models import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('template_name', 'created')
    list_filter = ('template_name', 'created')
    search_fields = ('template_name', 'template_body')
    date_hierarchy = 'created'
    ordering = ['created']


admin.site.register(Answer, AnswerAdmin)
