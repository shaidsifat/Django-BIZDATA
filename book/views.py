from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
import csv

from book.serializers import BookSerializer  
  
from .models import Book 
from django.http import HttpResponse
from .models import Book
from django.db.models import Max
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.db.models import Q

def getfile(request):  


    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = Book.objects.all()  
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.City,employee.Branch])  
    return response 


class BookList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

       
        
        snippets = Book.objects.all()
        serializer =  BookSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

         date1 = request.data['date1']
         date2 = request.data['date2']

         query= Book.objects.filter(
            Q(Date__gte=date1) & 
            Q(Date__lte=date2) 
         ).values('grossincome')
        # print(query)
         highest_value= query.aggregate(Max('grossincome'))
         print(highest_value)
         if date1 == None and  date2 == None:

            return Response({"grossincome__max":highest_value})

         else:
            return Response({"message":"none"})    
       
      