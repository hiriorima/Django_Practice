# coding: utf-8

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer, NestedUpdateMixin, NestedCreateMixin

from .models import Entry, HopeCareer, StudyArea, StudyTheme

import logging


class HopeCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopeCareer
        fields = '__all__'

class StudyThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTheme
        fields = '__all__'

class StudyAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyArea
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    
    study_theme = StudyThemeSerializer(allow_null=True)
    study_area = StudyAreaSerializer(allow_null=True)
    hope_career = HopeCareerSerializer(allow_null=True)
    
    class Meta:
        model = Entry
        fields = ('id', 'name', 'number', 'study_area', 'study_theme', 'progress_prepare', 'hope_career')

        # ネストされたモデルのPOSTに対応する
    def create(self, validated_data):

        study_theme_data = validated_data.pop('study_theme')
        study_theme = StudyTheme.objects.get_or_create(**study_theme_data)[0]
        validated_data['study_theme'] = study_theme
        hope_career_data = validated_data.pop('hope_career')
        hope_career = HopeCareer.objects.get_or_create(**hope_career_data)[0]
        validated_data['hope_career'] = hope_career
        study_area_data = validated_data.pop('study_area')
        study_area = StudyArea.objects.get_or_create(**study_area_data)[0]
        validated_data['study_area'] = study_area

        return Entry.objects.create(**validated_data)