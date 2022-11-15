from django.contrib import admin

from .models import Women


class WomenAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'content',
    )

admin.site.register(Women, WomenAdmin)
