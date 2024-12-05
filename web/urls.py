from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),  # Default route for the form
    path("success/", views.success, name="success"),
    path("book/", views.book_now, name="book"), 
]
