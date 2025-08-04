from django.contrib import admin
from .models import *
class BookAdmin(admin.ModelAdmin):
    fieldsets = []

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title',)
    ordering = ('publication_year',)
    readonly_fields = ('title', 'author')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
