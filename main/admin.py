from django.contrib import admin

from .models import Author, Book, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'category', 'author', 'image']
    list_filter = ['category', 'author']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
