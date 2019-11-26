from django.contrib import admin
from catalog.models import Author, Genre, Language, Book, BookInstance
# Register your models here.
# admin.site.register(Book)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstaceAdmin(admin.ModelAdmin):
     list_filter = ('status', 'due_back')
     list_display = ('book','status', 'due_back', 'id')
     fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields' : ('status', 'due_back')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)
