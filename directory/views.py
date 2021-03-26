from django.http import HttpResponse, HttpRequest

newwApp = """
<!DOCTYPE html>
<html>
<head>
<title>Teacher Directory </title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
        background: #AAAAAA;
    }
    div {
      padding: 30px;
      background: #FFFFFF;
      margin: 30px;
      border-radius: 5px;
      border: 1px solid #888888;
    }
    pre {
      padding: 15px;
    }
    code, pre {
      font-size: 16px;
      background: #DDDDDD
    }
</style>
</head>
<body>
  <div>
    <h1>Teacher Directory</h1>
   
  </div>
</body>
</html>
"""

def index(request):
    return HttpResponse(newwApp.replace("{IPADDRESS}",request.get_host()))
