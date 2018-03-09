from django.contrib import admin
from .models import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('template_name', 'created', 'updated')
    list_filter = ('template_name', 'created', 'updated')
    search_fields = ('template_name', 'template_body')
    date_hierarchy = 'created'
    ordering = ['created', 'updated']


admin.site.register(Answer, AnswerAdmin)
