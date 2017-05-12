from django.shortcuts import render
from .models import Application, ApplicationDependency
from django.http import JsonResponse

# Create your views here.
def index(request):
    result = {}

    nodes = []
    applications = Application.objects.all()
    for application in applications:
        nodes.append({"id": application.name, "group": 1})
    result["nodes"] = nodes

    links = []
    for application in applications:
        depends_on = application.get_application_by_depends_on()
        print(depends_on)
        for depend_on in depends_on:
            links.append({"source": application.name, "target": depend_on, "value": 1})
    result["links"] = links
    return JsonResponse(result)

def home(request):
    return render(request, 'home.html')
