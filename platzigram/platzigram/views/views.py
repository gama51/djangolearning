from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('oh, hi! current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def hello(request):
    numbers=request.GET['numbers'].split(",")
    data = {
        'status':'ok',
        'numbers':sorted([int(i) for i in numbers]),
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(json.dumps(data, indent=4),
    content_type='application/json'
    )
