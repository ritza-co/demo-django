from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person
# Create your views here.

def index(request):
    return render(request, 'helloworld/index.html')

def detail(request):
    users = Person.objects.all()
    context = {'users_list': users}
    return render(request, 'helloworld/all_users.html', context)

#@csrf_exempt
def submit(request):
    name = request.POST['name']
    person_object = Person(name=name)
    person_object.save()
    return render(request, 'helloworld/detail.html', {'name': name})
