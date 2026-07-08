from django.contrib import admin
from django.urls import include, path
from library.views import book_list, book_detail

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", book_list, name="book_list"),
    path("books/<int:book_id>/", book_detail, name="book_detail"),

    path("members/", include("members.urls")),
]