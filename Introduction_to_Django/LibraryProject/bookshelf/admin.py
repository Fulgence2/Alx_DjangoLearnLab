from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title',)
    ordering = ('title',)
    fields = ('title', 'author')
    readonly_fields = ('title', 'author')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        return obj
    save_as = save_model
