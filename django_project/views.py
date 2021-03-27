from django.http import HttpResponse, HttpRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.template import loader
MainProject = """
<!DOCTYPE html>
<html>
<head>
<title>Main Project </title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
        background: #AAAAAA;
    }
  
</style>
</head>
<body>
  <div>
    <h1>Main Project</h1>
   
  </div>
</body>
</html>
"""

admin = """
<!DOCTYPE html>
<html>
<head>
<title>Main Project </title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
        background: #AAAAAA;
    }
  
</style>
</head>
<body>
  <div>
    <h1>admin</h1>
   
  </div>
</body>
</html>
"""
def index(request):
    return HttpResponse(MainProject.replace("{IPADDRESS}",request.get_host()))

@staff_member_required
def my_admin_view(request):
    template = loader.get_template('directory/index.html')
    context = {
        'name': 'omer',
    }
    return HttpResponse(template.render(context, request))