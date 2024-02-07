from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST','GET'])
def books(request):
    return Response('list of the books',
                    status=status.HTTP_200_OK)