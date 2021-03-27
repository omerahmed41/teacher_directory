from django.db import models
from phone_field import PhoneField
from django.core.files.storage import default_storage
import os
import os.path
from os import path
from django.utils.html import mark_safe
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True        

  
class Subject(TimeStampMixin):
   name = models.CharField(max_length=30)
   class Meta:
        ordering = ['id']

   def __str__(self):
        return self.name
                
class Teacher (TimeStampMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField('profile_picture', blank=True) 
    email = models.EmailField(unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    room_number = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subjects = models.ManyToManyField(Subject)
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + ' ' +  self.last_name
        
