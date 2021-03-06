from django import forms
from bookstore.models import Customer
from bookstore.models import Book


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Customer's first name", widget=forms.TextInput(
        attrs={"placeholder": "customer's first name"}))
    last_name = forms.CharField(label="Customer's last name", widget=forms.TextInput(
        attrs={"placeholder": "customer's last name"}))
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={"placeholder": "YYYY-MM-DD"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"placeholder": "john@gmail.com"}))

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'email'
        ]


class BookForm(forms.ModelForm):
    title = forms.CharField(label="Book's title", widget=forms.TextInput(
        attrs={"placeholder": "book's title"}))
    author_first_name = forms.CharField(label="Author's first name", widget=forms.TextInput(
        attrs={"placeholder": "author's first name"}))
    author_last_name = forms.CharField(label="Author's last name", widget=forms.TextInput(
        attrs={"placeholder": "author's last name"}))
    price = forms.DecimalField()  # jeśli chcę domyślną wartość to initial=49.99
    book_description = forms.CharField(required=False,
                                       label="Description",
                                       widget=forms.Textarea(
                                           attrs={  # atrybutes of textarea field
                                               "placeholder": "provide a description of the book",
                                               "class": "nowa-klasa",
                                               "id": "id-for-textfield",
                                               "rows": 5,
                                               "cols": 50
                                           }
                                       )
                                       )

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Book
        fields = [
            'title',
            'author_first_name',
            'author_last_name',
            'price',
            'book_description'
        ]


class OrderBookForm(forms.ModelForm):

    customers = Customer.objects.all()
    customers_ids = []
    for customer in customers:
        customers_ids.append(customer.id)

    # customers_data = []
    # for customer in customers:
    #     customers_data.append((customer.id, customer.first_name))

    # tak było, gdy tylko id się wyświetlało w drop down list
    # CUSTOMER_CHOICES = [tuple([x, x]) for x in customers_ids]

    # to jest lista krotek, która jest uogólniona w pętli poniżej
    # CUSTOMER_CHOICES = [
    #     (1, Customer.objects.filter(id=1)),
    #     (2, Customer.objects.filter(id=2)),
    #     (3, Customer.objects.filter(id=3)),
    # ]

    CUSTOMER_CHOICES = []
    for i in customers_ids:
        CUSTOMER_CHOICES.append((i, Customer.objects.get(id=i)))

    buyer_id = forms.DecimalField(label="Enter the customer id from the customer list below",
                                  widget=forms.Select(choices=CUSTOMER_CHOICES)
                                  # widget=forms.TextInput(attrs={"placeholder": "customer id"}) # gdy było zwykłe pole
                                  )

    class Meta:
        nazwa = forms.CharField(label='',
            widget=forms.TextInput(attrs={"placeholder": "Wpisz nazwę"}))  # etykieta Nazwa się nie pojawi bo label=''
        model = Book
        fields = [
            'buyer_id'
        ]

    # walidacja pola buyer_id (ale nie używam bo jest drop down list zamiast zwykłego TextInput)
    # def clean_buyer_id(self, *args, **kwargs):
    #     buyer_id = self.cleaned_data.get("buyer_id")
    #     try:
    #         Customer.objects.get(id=buyer_id)
    #         return buyer_id
    #     except:
    #         print("This customer does not exist (from print)")