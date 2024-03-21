from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# @api_view(['POST','GET'])
# def books(request):
#     return Response('list of the books',
#                     status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if (author):
            return Response({'author':author},status.HTTP_200_OK)
        return Response({'msg':'from class get2'},
                        status.HTTP_200_OK)

    def post(self,request):
        bookTitle = request.data.get('title')
        if (bookTitle):
            return Response({'title':bookTitle},status.HTTP_201_CREATED)
        return Response({'msg':'class post method'},
                        status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, request, pk):
        return Response({'book id':str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({'id and titled':str(pk) + request.data.get('title'),
                         },status.HTTP_200_OK)