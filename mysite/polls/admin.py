from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/1.11/intro/tutorial07/
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,          {
            'fields': ['question_text']
        }),
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        })
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)