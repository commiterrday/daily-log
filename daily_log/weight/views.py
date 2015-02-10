from django.shortcuts import render
from django.http import HttpResponse

from weight.models import Weight

# Create your views here.
def index(request):
    allpts = Weight.objects.all()
    output = '<ul>\n'
    output += '\n'.join(
            ['<li>' + str(w.time) + ': %.1f kg %.1f%% BF</li>' % (w.kg, w.body_fat) for w in allpts]
            )
    output += '</ul>\n'
    return HttpResponse(output)
