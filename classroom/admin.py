
from django.contrib import admin
from .models import Question,Archive,Schedule,Slide
from django.utils.html import format_html

#class schAdmin(admin.ModelAdmin):
 #   list_display1 = ( 'topic','duration','schedule_date')
#admin.site.register(Schedule, schAdmin)

#@admin.register(models.Question)
'''class URLFieldWidget(AdminURLFieldWidget):
	def render(self,name,value,attrs=None):
		widget=super(URLFieldWidget,self).render(name,value,attrs)
		return mark_safe(u'%s&nbsp;&nbsp;<input type="button">'
						u'value="View Link" onclick="window'
						u'open(document.getElementById(\'%s\')'
						u',value)"/> % (widget,attrs['id']))'''
class queAdmin(admin.ModelAdmin):
    list_display1 = ( 'id','ques_link','question_date')
    
    '''def ques_link(self,obj):
    	return format_html("<a href='%s'>{url}</a>", % (obj.url,obj.url)
    ques_link.allow_tags=True
    ques_link.short_description="URL"'''

admin.site.register(Question, queAdmin)

class archiveAdmin(admin.ModelAdmin):
    list_display1 = ( 'session')
admin.site.register(Archive, archiveAdmin)

class slideAdmin(admin.ModelAdmin):
    list_display1 = ( 'id','url','question_date')
admin.site.register(Slide, slideAdmin)

class scheduleAdmin(admin.ModelAdmin):
    list_display1 = ( 'id','url','question_date')
admin.site.register(Schedule, scheduleAdmin)
