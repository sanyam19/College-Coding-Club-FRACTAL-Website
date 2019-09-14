from django.db import models
import os
from django.utils import timezone
class Question(models.Model):
    heading=models.CharField(max_length=200)
    url=models.URLField(max_length=555,blank=True,null=True)
    question_date = models.DateTimeField(
            default=timezone.now)
    session=models.ForeignKey('Archive',on_delete=models.CASCADE,null=True)
    #tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.heading
class Slide(models.Model):
        heading=models.CharField(max_length=200,null=True)
        url=models.URLField(max_length=555,blank=True,null=True)
        question_date = models.DateTimeField(
            default=timezone.now)
        session=models.ForeignKey('Archive',on_delete=models.CASCADE,null=True)
class Archive(models.Model):
    session=models.CharField(max_length=60)  # since 2017-18 contains "-" character

    def __str__(self):
        return self.session

    class Meta:                   # ordering ka mtlb sorting (here sorting the results by headline)
        ordering = ('session',)        
class Schedule(models.Model):
    topic=models.CharField(max_length=200)
    duration=models.IntegerField(default=0)
    schedule_date = models.DateTimeField(
            default=timezone.now)