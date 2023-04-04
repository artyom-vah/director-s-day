from django.contrib import admin
from .models import *

# admin.site.register(Division)
# admin.site.register(Enterprise)
# admin.site.register(Question)
# admin.site.register(QuestionStats)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')
    list_filter = ('name', 'division')
    search_fields = ('name', 'division')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'enterprise', 'question', 'email')
    list_filter = ('enterprise',)
    search_fields = ('date_time', 'enterprise', 'question', 'email')

#
# @admin.register(QuestionStats)
# class QuestionStatsAdmin(admin.ModelAdmin):
    # list_display = ('division', 'enterprise', 'question_count')
    # list_filter = ('division', 'enterprise', 'question_count')
    # search_fields = ('division', 'enterprise', 'question_count')
