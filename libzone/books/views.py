from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic import DeleteView
from .models import Book, Category
# Create your views here.

class BookView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()

        cat_slug  = kwargs.get('cat_slug',None) 

        if cat_slug:
            category = Category.objects.get(slug=cat_slug)
            books = Book.objects.filter(category=category)

        context['books'] = books
        context['categorys'] = Category.objects.all()

        return context
     
class BookDetailsView(DeleteView):
    template_name = 'book_details.html'
    model = Book
    pk_url_kwarg = 'book_id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_id = self.kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)
        context['book'] = book 

        return context  