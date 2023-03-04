from django.http import HttpResponse,HttpRequest,JsonResponse
import json

def index(request:HttpRequest):
    """
    This is the index view get request
    args:
        request:HttpRequest
    return:
        HttpResponse
    """
    # get the data from the request
    data=request.GET 
    # get the value of a if not found return 0
    a = int(data.get('a',0)) 
    # get the value of b if not found return 0
    b = int(data.get('b',0)) 
    return JsonResponse({'sum':a+b})

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
    