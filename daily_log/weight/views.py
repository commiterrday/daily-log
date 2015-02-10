from django.shortcuts import render
from django.http import JsonResponse

from weight.models import Weight


def index(request):
    points = Weight.objects.all()
    context = {'points': points }
    return render(request, 'weight/index.html', context)


def alljson(request):
    # Convert to List, since ValueListQuerySet is not JSON-serializable
    # Ref: http://blog.mourafiq.com/post/47739842739/is-not-json-serializable-django
    points = list(Weight.objects.values('time', 'kg', 'body_fat'))

    #for p in points:
    #    p['time'] = str(p['time']) # TODO: avoid losing the TZ

    return JsonResponse({'points': points })
