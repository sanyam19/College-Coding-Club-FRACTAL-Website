from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch=models.CharField(max_length=200, blank=True,null=True)
    rollno=models.CharField(max_length=200, blank=True,null=True)
    phone=models.CharField(max_length=13, blank=True,null=True)
    token=models.CharField(max_length=200,blank=True,null=True)
    sessions=models.CharField(max_length=200,blank=True,null=True,default='2018-2019')
    #username=re.sub(name)+'_'+str(rollno[:2])+str(rollno[6:])
    def __str__(self):
        return self.rollno

      


class Upload(models.Model):
    pic = models.FileField(upload_to="media/")    
    upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('pic',)        
'''
class Questions(models.Model):
    #user = models.ForeignKey('User',
         #on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True,blank=True)  
    url=models.URLField(max_length=555,blank=True,null=True)
    tags = models.ManyToManyField('Tag')
    category = models.ManyToManyField('Category')
    question_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title 

    def display_tags(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(tags.tag_name for tags in self.tags.all()[:3])
    
    display_tags.short_description = 'Tag'   

    def display_category(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(category.category_name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category' 


class Tag(models.Model):
    tag_name =models.CharField(max_length=200, null=True,blank=True)	

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    difficulty = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
           )
    category_name = models.CharField(
        max_length=1,
        choices=difficulty,
        blank=True,
        default='E',
    )
   
    def __str__(self):
        return self.category_name

class Tokens(models.Model):
    token=models.CharField(max_length=250,blank=True,unique=True,null=True)
    
    def __str__(self):
        return self.token
    
class Classroom(models.Model):
    heading=models.CharField(max_length=200)
    url=models.URLField(max_length=555,blank=True,null=True)
    question_date = models.DateTimeField(
            default=timezone.now)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.heading
'''
