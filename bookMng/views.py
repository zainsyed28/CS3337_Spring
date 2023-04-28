from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import MainMenu
from .forms import BookForm
from .forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Book
from .models import Comment

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                  }
                  )


def displaybooks(request):
    books = Book.objects.all()
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    comments = Comment.objects.filter(book_origin=book)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.username = request.user
            except Exception:
                pass
            comment.book_origin = book
            comment.save()
    else:
        form = CommentForm()

    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'form': form,
                      'comments': comments,
                  }
                  )


def mybooks(request):
    books = Book.objects.filter(username=request.user)
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


def about_us(request):
    return render(request,
                  'bookMng/about_us.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


def favorite_add(request, id):
    book = Book.objects.get(id=id)
    if book.favorites.filter(id=request.user.id).exists():
        book.favorites.remove(request.user)
    else:
        book.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favorites(request):
    username = request.user
    books = Book.objects.filter(favorites=request.user)
    return render(request,
                  'bookMng/favorite_books.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )
