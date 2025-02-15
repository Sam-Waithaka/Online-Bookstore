from django.contrib import admin

from .models import Book, Review

# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = (ReviewInline,)
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('title',)


admin.site.register(Book, BookAdmin)