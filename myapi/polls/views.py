from django.shortcuts import render
from rest_framework import permissions
from .models import Partfolio
from .serializer import PersonSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class MyWorkView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Partfolio.objects.all()
    serializer_class = PersonSerializer

    # # First
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class MyWorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Partfolio.objects.all()
    serializer_class = PersonSerializer
