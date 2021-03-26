from django.http import HttpResponse, HttpRequest

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

def index(request):
    return HttpResponse(MainProject.replace("{IPADDRESS}",request.get_host()))
