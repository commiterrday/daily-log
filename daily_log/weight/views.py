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

    # Security concerns: is JSON/Array [1] an issue with the nested array? Note this isn't
    # an issue with EcmaScript 5, according to the Django docs [2].
    # [1] http://incompleteness.me/blog/2007/03/05/json-is-not-as-safe-as-people-think-it-is/
    # [2] https://docs.djangoproject.com/en/1.7/ref/request-response/#serializing-non-dictionary-objects
    return JsonResponse({'points': points })
