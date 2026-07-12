from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm, ReviewForm

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all().order_by("-created_at")
    return render(request, "library/book_detail.html", {"book": book, "reviews": reviews})

@login_required(login_url="login")
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/book_form.html", {"form": form})

@login_required(login_url="login")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)

    else:
        form = BookForm(instance=book)

    return render(request, "library/book_form.html", {"form": form})

@login_required(login_url="login")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "library/delete_book.html", {"book": book})


@login_required(login_url="login")
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    existing_review = book.reviews.filter(user=request.user).first()

    if existing_review:
        return redirect("book_detail", book_id=book.id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect("book_detail", book_id=book.id)

    else:
        form = ReviewForm()

    return render(request, "library/review_form.html", {"form": form, "book": book})
