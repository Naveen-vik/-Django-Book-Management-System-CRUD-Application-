from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'testapp/book.html' #customize template
    context_object_name = 'books'
    #default template file : book_list.html
    #default context object name: book_list

class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html' #customize template
    context_object_name = 'books'

class BookDetailsView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')


