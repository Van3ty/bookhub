from django.contrib import admin
from django.urls import include, path
from library.views import book_list, book_detail, add_book, edit_book, delete_book, add_review

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", book_list, name="book_list"),
    path("books/<int:book_id>/", book_detail, name="book_detail"),
    path("books/add/", add_book, name="add_book"),
    path("books/<int:book_id>/edit/", edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", delete_book, name="delete_book"),
    path("books/<int:book_id>/reviews/add/", add_review, name="add_review"),
    path("members/", include("members.urls")),

]
