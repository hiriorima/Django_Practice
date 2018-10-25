# coding: utf-8

from rest_framework import routers
from .views import EntryViewSet, HopeCareerViewSet, StudyThemeViewSet, StudyAreaViewSet

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'career', HopeCareerViewSet)
router.register(r'theme', StudyThemeViewSet)
router.register(r'area', StudyAreaViewSet)