from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


# Create your views here.
class ProductListCreateApiView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
