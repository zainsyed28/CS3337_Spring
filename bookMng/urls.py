from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('aboutus', views.about_us, name='aboutus'),
    path('favorite/<int:id>', views.favorite_add, name='favorite_add'),
    path('favorite_books', views.favorites, name='favorite_book')
]


