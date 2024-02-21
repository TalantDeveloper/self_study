from django.contrib import admin
from .models import *


class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'count_options']
    list_filter = ['title']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'description', 'get_options', 'get_corrects']


class CreditAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'description', 'get_questions']
    list_display_links = ['id', 'slug', 'title']


admin.site.register(Option, OptionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Credit, CreditAdmin)
