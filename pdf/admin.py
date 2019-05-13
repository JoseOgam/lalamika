from django.contrib import admin
from . import models


# Register your models here.

class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('user', 'semester', 'unit', 'marks')
    list_per_page = 50
    list_editable = ('marks',)
    search_fields = ('marks',)
    list_filter = ('user',)


admin.site.register(models.Transcript, TranscriptAdmin)
admin.site.register(models.Semester)
admin.site.register(models.Unit)
