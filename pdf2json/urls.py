from django.urls import path

from . import views

urlpatterns = [
    path("", views.pdf_reader, name="pdf_reader"),
]
