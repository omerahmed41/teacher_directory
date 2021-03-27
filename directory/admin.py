from django.contrib import admin
from .models import Subject
from .models import Teacher
from django.core.exceptions import ValidationError
from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class LastNameFirstLetterFilter(admin.SimpleListFilter):
   
    title = _('LastName FirstLetter')

    parameter_name = 'decade'

    def lookups(self, request, model_admin):
          teachers = Teacher.objects.all().distinct()
          list_teacher = []
          for teacher in teachers:
             raw =  ( teacher.last_name[0], teacher.last_name[0])
             if raw not in list_teacher:
                list_teacher.append( raw )
          return (
              sorted(list_teacher, key=lambda tp:tp[1])
          )
    def queryset(self, request, queryset):
        
        if self.value() != None  :
           
            return queryset.filter(last_name__startswith=self.value())


class SubjectAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Subject, SubjectAdmin)


class TeacherForm(forms.ModelForm):
    model = Teacher
    fields = ('image_tag','profile_picture', 'fisrt_name', 'last_name')
    readonly_fields = ('image_tag',)
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('subjects').count() > 5:
            raise ValidationError('You have to choose exactly 5 subjects per Teacher ')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ('id','upper_case_name','email')
    list_filter = ['last_name', 'subjects',LastNameFirstLetterFilter]
    search_fields = ['email']
    
    def upper_case_name(self, obj):
       return ("%s %s" % (obj.first_name, obj.last_name)).upper()
    upper_case_name.short_description = 'Name'
    
 