from django.db import models
from phone_field import PhoneField


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
    profile_picture = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    room_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subjects = models.ManyToManyField(Subject)
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name
        
      
         
    