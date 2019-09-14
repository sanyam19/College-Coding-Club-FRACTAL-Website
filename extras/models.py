from django.db import models
from django.utils import timezone

class Questions(models.Model):
    #user = models.ForeignKey('User',
    #on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True,blank=True)
    url=models.URLField(null=True,blank=True,default='')
    tags = models.ManyToManyField('Tag')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    question_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title 

    def display_tags(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(tags.tag_name for tags in self.tags.all()[:3])
    
    display_tags.short_description = 'Tag'   

   # def display_category(self):
    #"""Create a string for the Genre. This is required to display genre in Admin."""
       # return ', '.join(category.category_name for category in self.category.all()#[:3])
    
   # display_category.short_description = 'Category' 

class Archive(models.Model):
	session=models.CharField(max_length=200)

	def __str__(self):
		return self.session

class resourses(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)  
    url=models.URLField(null=True,blank=True,default='')
    tags = models.ManyToManyField('Tag')
   
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title 

    def display_tags1(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(tags.tag_name for tags in self.tags.all()[:3])
    
    display_tags1.short_description = 'Tag' 



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
# Create your models here.
