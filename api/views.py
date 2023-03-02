from django.http import HttpResponse,HttpRequest,JsonResponse

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

