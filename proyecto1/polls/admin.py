from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

#Clases modelAdmin.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    search_fields = ["question_text"]
    list_filter = ('question_text',)
    inlines = [ChoiceInline]

#Clases modelAdmin.
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")
    search_fields = ["choice_text"]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)