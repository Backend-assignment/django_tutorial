from django.http import HttpResponse,HttpRequest,JsonResponse
import json
# Import the models
from .models import Person

def index(request:HttpRequest):
    person = Person.objects.all()
    person[0].delete()
    
    
    

    return JsonResponse({'message':'Hello World'})
  

# Define the view

def get_data(request:HttpRequest):
    """
    This is the get data view get request
    args:
        request:HttpRequest
    return:
        HttpResponse
    """
    # Check if the request is POST
    if request.method == "POST":
        data = request.body.decode()
        print(json.loads(data))

    # Check if the request is GET
    if request.method == "GET":
        print('GET')


    return HttpResponse('Hello World')
    