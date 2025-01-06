from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView

from django.views.generic import DeleteView
from .models import Book, Category
# Create your views here.

from django.shortcuts import redirect

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
     

from review.forms import CommentForm

class BookDetailsView(FormView):
    template_name = 'book_details.html'
    model = Book
    pk_url_kwarg = 'book_id' 
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_id = self.kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)
        context['book'] = book 
        context['related_books'] = Book.objects.all()[:5]
        
        context['similar_category_books'] = []
        for cat in book.category.all():
            some_books = Book.objects.filter(category=cat).exclude(id=book.id)  # Get books in the same category, excluding the current book
            context['similar_category_books'].extend(some_books)  # Append the books to the list

        context['comment_form'] = self.form_class()
        context['comments'] = book.comments.all()  # Assuming the `Book` model has a related_name 'comments'

        return context  
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        book_id = kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)

        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect('login')
            # Save the form with additional data
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            return redirect('books_details',book_id=book_id)

        # Redirect back to the book details page
        return self.get(request, *args, **kwargs)