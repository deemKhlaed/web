from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name="books.html5.links"),
 path('html5/text/formatting', views.text, name="books.html5.text"),
 path('html5/text/listing', views.text2, name="books.html5.text2"),
 path('html5/table/', views.table, name="books.html5.table"),
 path('search/', views.search, name="books.search"),
path('simple_query/', views.simple_query, name="books.simple_query"),
path('complex_query/', views.complex_query, name="books.complex_query"),
 
]