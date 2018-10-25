from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class HopeCareer(models.Model):
    desire = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    region = models.CharField(max_length=32)
    job_category = models.CharField(max_length=32)

class StudyTheme(models.Model):
    theme = models.CharField(max_length=32)
    body = models.TextField()

class StudyArea(models.Model):
    area = models.CharField(max_length=32)

class Entry(models.Model):
    name = models.CharField(max_length=32)
    number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300000)])
    study_area = models.ForeignKey(StudyArea, on_delete=models.CASCADE, related_name='study_area')
    study_theme = models.ForeignKey(StudyTheme, on_delete=models.CASCADE, related_name='study_theme')
    progress_prepare = models.TextField()
    hope_career = models.ForeignKey(HopeCareer, on_delete=models.CASCADE, related_name='hope_career')
    # study_area = models.ManyToManyField(StudyArea)
    # study_theme = models.ManyToManyField(StudyTheme)
    # hope_career = models.ManyToManyField(HopeCareer)