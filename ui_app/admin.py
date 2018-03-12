from django.contrib import admin
from .models import Answer

<<<<<<< HEAD
admin.site.register(Answer)
=======

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('template_name', 'created', 'updated')
    list_filter = ('template_name', 'created', 'updated')
    search_fields = ('template_name', 'template_body')
    date_hierarchy = 'created'
    ordering = ['created', 'updated']


admin.site.register(Answer, AnswerAdmin)
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
