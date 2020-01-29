from django.shortcuts import render


def books(request):
    context = {}
    return render(request, "books/books.html", context=context)
