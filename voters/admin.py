from django.contrib import admin
from .models import Voter

# Register your models here.


class VoterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Voter', {'fields': ['tg_id', 'year', 'faculty', 'gender']})
    ]

admin.site.register(Voter, VoterAdmin)
