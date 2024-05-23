from django.shortcuts import render
from.models import *
from.serializer import Resumeserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Resume_view(APIView):
    def post(self,request):
        serializer = Resumeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Resume upload successfully",'status':"success",'candidate':serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)