from django.contrib import admin
from .models import VotedPoll, Vote
# Register your models here.


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1
    fieldsets = [
        (None, {'fields': ['faculty', 'year', 'choice']})
    ]


class VotePollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Voted Poll', {'fields': ['poll_name', ]})
    ]
    inlines = [VoteInline]

admin.site.register(VotedPoll, VotePollAdmin)
