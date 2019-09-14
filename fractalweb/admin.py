from django.contrib import admin
from .models import ExtendedUser,Upload
from extras.models import Questions,Tag,Category
from classroom.models import Question,Archive

admin.site.register(ExtendedUser)
admin.site.register(Upload)


#admin.site.register(Questions)
#admin.site.register(Tag)
#dmin.site.register(Category)
#admin.site.register(Question)

#class QuestionAdmin(admin.ModelAdmin):
 #   list_display = ( 'title','display_tags','display_category')

#admin.site.register(Questions, QuestionAdmin)
