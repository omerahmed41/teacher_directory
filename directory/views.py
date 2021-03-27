from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
import csv, io
from django.contrib import messages
from .models import Teacher
from .models import Subject
import re
import ast


def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

pleaseLogin = """  <h1>Please Login</h1>"""

def index(request):
    return HttpResponse(newwApp.replace("{IPADDRESS}",request.get_host()))



def teatcher_import(request):
   template = loader.get_template('directory/index.html')
   context = {'name': 'omer'}
   if request.user.is_superuser:
     return render(request, 'directory/index.html', context)
   else:
      return HttpResponse(pleaseLogin.replace("{IPADDRESS}",request.get_host()))
      
      
def profile_upload(request):
    
    # declaring template
    template = "directory/profile_upload.html"
    data = Teacher.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be First Name,	Last Name,	Profile picture,	Email Addres,s	Phone Number,	Room Number,	Subjects taught',
        'teachers': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
         return render(request, template, prompt)
         
    if request.method == "POST":
          messages.add_message(request, messages.INFO, 'Teachers imported Successfully.')    
    csv_file = request.FILES['file']
    
    # let's check if it is a csv file
    logs = []
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for row  in csv.reader(io_string,delimiter=','):         
          if valid_email(row [3]):  
              teacher, created = Teacher.objects.update_or_create(
                  first_name=row [0],
                  last_name=row [1],
                  profile_picture=row [2],
                  email=row [3],
                  phone_number=row [4],
                  room_number=row [5],
                  
              )
             
              subjects_str = row [6]
              subjects_names = subjects_str.split(", ")              
              subjects_names = map(str.lower, subjects_names) # normalize them, all lowercase
              subjects_names = list(set(subjects_names)) # remove duplicates
              added_subjects = []             
              for subject_name in subjects_names:                  
                  print (subject_name)
                  subject, _ = Subject.objects.get_or_create(name=subject_name)                
                  Teachers = Teacher.objects.get(id=teacher.id)               
                  if  Teachers.subjects.count() < 6:
                      Teachers.subjects.add(subject ) 
                      added_subjects.append(subject_name)
                      
              log =  {teacher.first_name: added_subjects}
              logs.append(log)    
                  
    context = {'teachers': data, 'logs': logs  }
    return render(request, template, context)      