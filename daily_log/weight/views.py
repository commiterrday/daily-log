from django.shortcuts import render

from weight.models import Weight

# Create your views here.
def index(request):
    points = Weight.objects.all()
    context = {'points': points }
    return render(request, 'weight/index.html', context)
