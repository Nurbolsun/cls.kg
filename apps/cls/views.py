from django.shortcuts import render
from .serializers import BranchSerializer, BranchImageSerializer, RegionSerializer
from .models import Branch, BranchImage, Region
from rest_framework import viewsets


# Create your views here.
class BranchAPIList(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchImageAPIList(viewsets.ModelViewSet):
    queryset = BranchImage.objects.all()
    serializer_class = BranchImageSerializer


class RegionAPIList(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
