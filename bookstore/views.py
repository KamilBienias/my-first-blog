from django.shortcuts import render, redirect
from bookstore.models import Customer
from bookstore.models import Book
from bookstore.forms import CustomerForm
from bookstore.forms import BookForm
from bookstore.forms import OrderBookForm


def bookstore_home_page(request):
    return render(request, "bookstore/bookstore.html")


def create_customer(request):
    form = CustomerForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = CustomerForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/bookstore/customer/new/added")
    context = {
        'form': form
    }
    return render(request, "bookstore/customers/createcustomer.html", context)


def customer_added_successfully(request):
    customers = Customer.objects.all()
    customers_ids = []
    for customer in customers:
        customers_ids.append(customer.id)

    added_customer = Customer.objects.get(id=customers_ids[-1])

    context = {
        'added_customer': added_customer
    }
    return render(request, "bookstore/customers/customeraddedsuccessfully.html", context)


def create_book(request):
    form = BookForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = BookForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/bookstore/book/new/added")
    context = {
        'form': form
    }
    return render(request, "bookstore/books/createbook.html", context)


def book_added_successfully(request):
    books = Book.objects.all()
    books_ids = []
    for book in books:
        books_ids.append(book.id)

    added_book = Book.objects.get(id=books_ids[-1])

    context = {
        'added_book': added_book
    }
    return render(request, "bookstore/books/bookaddedsuccessfully.html", context)


def all_books(request):

    books = Book.objects.order_by('id')

    context = {
        'books': books
    }
    return render(request, "bookstore/books/allbooks.html", context)


def all_customers(request):
    customers = Customer.objects.order_by('id')

    context = {
        'customers': customers
    }
    return render(request, "bookstore/customers/allcustomers.html", context)


def show_books_to_order(request):
    books = Book.objects.order_by('id')
    context = {
        'books': books
    }
    return render(request, "bookstore/customers/showbookstoorder.html", context)


def select_buyer(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = OrderBookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save(commit=True)
        form = OrderBookForm()  # odświeża formularz, po zapisaniu będą puste pola
    else:
        form = OrderBookForm()  # na GET dostaję pusty formularz
    customers = Customer.objects.order_by('id')
    context = {
        'form': form,
        'customers': customers,
        'book': book
    }
    return render(request, "bookstore/customers/selectbuyer.html", context)


def show_bought_books_by_selected_customer(request, id):
    selected_customer = Customer.objects.get(id=id)
    books = Book.objects.filter(buyer_id=id)
    context = {
        'selected_customer': selected_customer,
        'books': books
    }
    return render(request, "bookstore/customers/boughtbooks.html", context)