from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Category

# Create your views here.
def book_list(request, category_slug=None, author_slug=None):
    categories = Category.objects.all()
    books = Book.objects.all()

    category = None
    author = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        books = books.filter(author=author)
    return render(request, 'main/book/list.html',
                  context={'category': category,
                           'author': author,
                           'categories': categories,
                           'books': books})

def book_detail(request, book_slug=None):
    categories = Category.objects.all()
    book = get_object_or_404(Book, slug=book_slug)
    return render(request, 'main/book/detail.html', context={'categories': categories, 'book': book})