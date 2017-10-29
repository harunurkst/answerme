from django.contrib import admin

from .models import Question
from answer.models import Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text','user','created','upvote')
    inlines = [AnswerInline]
