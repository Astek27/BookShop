from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
     path('', views.book_list, name='book_list'),
     path('category/<slug:category_slug>', views.book_list,
          name='book_list_by_category'),
     path('author/<slug:author_slug>', views.book_list,
          name='book_list_by_author'),
     path('book/<slug:book_slug>', views.book_detail,
          name='book_detail')
]
