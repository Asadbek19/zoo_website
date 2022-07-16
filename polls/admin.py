from django.contrib import admin

from .models import (
    Question,
    Choice,
    Event
)
# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

# admin.site.register(Event)


@admin.register(Event)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'timestamp',
        'text'
    ]
