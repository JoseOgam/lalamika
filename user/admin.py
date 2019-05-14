from django.contrib import admin

from user.models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'regno', 'user', 'sem')
    list_per_page = 50
    list_editable = ('regno',)
    search_fields = ('regno',)
    list_filter = ('user',)


admin.site.register(UserProfile)
