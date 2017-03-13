from django.shortcuts import render
import json

# Create your views here.

def index(request):
    final_data = json.load(open("rain/data.json"))
    context = {'data': final_data}
    return render(request, "rain/index.html", context)
