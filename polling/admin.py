from django.contrib import admin
from .models import Poll, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll', {'fields': ['poll_name', 'poll_question', 'opening_date', 'closing_date', ]})
    ]

    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)
