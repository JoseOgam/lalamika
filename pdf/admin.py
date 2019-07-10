from django.contrib import admin
from . import models


# Register your models here.

class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('user', 'semester')
    list_per_page = 50
    list_filter = ('user',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'status')
    list_per_page = 50
    list_editable = ('status',)

    class LecturerAdmin(admin.ModelAdmin):
        list_display = ('name', 'unit', 'semester', 'transcript')


admin.site.register(models.Transcript, TranscriptAdmin)
admin.site.register(models.Complaints, ComplaintAdmin)
admin.site.register(models.Semester)
admin.site.register(models.Unit)
admin.site.register(models.Result)
admin.site.register(models.Lecturer)
