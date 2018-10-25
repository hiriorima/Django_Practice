# coding: utf-8

import django_filters
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.response import Response

from .models import Entry, HopeCareer, StudyArea, StudyTheme
from .serializers import EntrySerializer, HopeCareerSerializer, StudyThemeSerializer, StudyAreaSerializer

class HopeCareerViewSet(viewsets.ModelViewSet):
    queryset = HopeCareer.objects.all()
    serializer_class = HopeCareerSerializer

class StudyThemeViewSet(viewsets.ModelViewSet):
    queryset = StudyTheme.objects.all()
    serializer_class = StudyThemeSerializer

class StudyAreaViewSet(viewsets.ModelViewSet):
    queryset = StudyArea.objects.all()
    serializer_class = StudyAreaSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer