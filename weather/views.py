from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.

def home(request):
    if request.method=="POST":
        city=request.POST.get('city')
        city=city.replace(" ","+")
        API_KEY='da9b058e845847798e253530210405'
        source='0'
        try:
            source=urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+city).read()
        except Exception:
            data={
            "text":"No matching location found."
            }
            return render(request, 'weather.html',data)
        list_of_data=json.loads(source)
        if list_of_data:
            print(list_of_data)
            data={
                'name':str(list_of_data['location']['name']),
                'coordinates':{
                'longitude': str(list_of_data['location']['lon']),
                'latitude': str(list_of_data['location']['lat']),
                },
                'pressure': str(list_of_data['current']['pressure_mb']),
                'humidity': str(list_of_data['current']['humidity']),
                'wind': str(list_of_data['current']['wind_kph']),
                'temp': str(list_of_data['current']['temp_c']),
                'text': str(list_of_data['current']['condition']['text']),
                'local_time': str(list_of_data['location']['localtime']),

            }
            # return render(request, 'weather.html',data)
        else:
            print("empty")
            data = {
                "text": "No matching location found."
            }
    else:
        data={}




    return render(request, 'weather.html',data)
