from django.contrib import admin
from .models import Questions,Tag,Category,resourses

#admin.site.register(Questions)
admin.site.register(Tag)
admin.site.register(Category)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'title','display_tags','category')
admin.site.register(Questions, QuestionAdmin)

class resorAdmin(admin.ModelAdmin):
    list_display1 = ( 'display_tags1','title','url','date')
admin.site.register(resourses, resorAdmin)
# Register your models here.