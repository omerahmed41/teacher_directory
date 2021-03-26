from django.contrib import admin
from .models import Subject
from .models import Teacher
from django.core.exceptions import ValidationError
from django import forms

admin.site.register(Subject)



class TeacherForm(forms.ModelForm):
    model = Teacher

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('subjects').count() > 5:
            raise ValidationError('You have to choose exactly 5 subjects per Teacher ')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    

    