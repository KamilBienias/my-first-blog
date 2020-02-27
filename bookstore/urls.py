from django.urls import path
from . import views

urlpatterns = [
    path('customer/new/', views.create_customer, name='create_customer'),
    path('customer/new/added', views.customer_added_successfully, name='customer_added_successfully'),
    path('customer/all/', views.all_customers, name='all_customers'),
    path('customer/all/<int:id>', views.show_bought_books_by_selected_customer, name='show_bought_books_by_selected_customer'),
    path('customer/order/', views.show_books_to_order, name='show_books_to_order'),
    path('customer/order/<int:id>', views.select_buyer, name='select_buyer'), # Django spodziewa się liczby całkowitej i przekaże jej wartość do widoku jako zmienną id
    path('book/new/', views.create_book, name='create_book'),
    path('book/new/added/', views.book_added_successfully, name='book_added_successfully'),
    path('book/all/', views.all_books, name='all_books'),
    path('', views.bookstore_home_page, name='bookstore_home_page'),
]