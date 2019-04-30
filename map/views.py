from django.shortcuts import render
import csv
import itertools
# Create your views here.
from .models import City
from .forms import Searchform


def Home(request):
    
    form = Searchform(request.POST or None)
    template = "map/home.html"
    context = {}

    if form.is_valid():
        # print(request.POST)
        place_name = form.cleaned_data.get('place_name').lower()
        data = City.objects.filter(place_name=place_name)
        # print(data)
        country_code = data[0].country_code #data.get("country_code")
        pincode =  data[0].pincode #data.get("pincode")
        place_name = data[0].place_name #data.get("place_name")
        admin_name1 =  data[0].admin_name1 #data.get("admin_name1")
        admin_name2 =  data[0].admin_name2 #data.get("admin_name2")
        admin_name3 = data[0].admin_name2 #data.get("admin_name3")
        latitude = data[0].latitude #data.get("latitude")
        longitude = data[0].longitude #data.get("longitude")
        accuracy = data[0].accuracy #data.get("accuracy")
        malaria_cause = data[0].malaria_cause #data.get("malaria_cause")
        malaria_deaths = data[0].malaria_deaths #data.get("malaria_deaths")
        malnutrition_cause = data[0].malnutrition_cause #data.get("malnutrition_cause")
        malnutrition_deaths = data[0].malnutrition_deaths #data.get("malnutrition_deaths")
        tuberculosis_cause = data[0].tuberculosis_cause #data.get("tuberculosis_cause")
        tuberculosis_deaths = data[0].tuberculosis_deaths #data.get("tuberculosis_deaths")
        population = data[0].population #data.get("population")
        malaria_risk_factor = data[0].malaria_risk_factor #data.get("malaria_risk_factor")
        malnutrition_risk_factor = data[0].malnutrition_risk_factor #data.get("malnutrition_risk_factor")
        tuberculosis_risk_factor = data[0].tuberculosis_risk_factor #data.get("tuberculosis_risk_factor")
        malaria_risk_index =  data[0].malaria_risk_index #data.get("malaria_risk_index")
        malnutrition_risk_index = data[0].malnutrition_risk_index #data.get("malnutrition_risk_index")
        tuberculosis_risk_index = data[0].tuberculosis_risk_index #data.get("tuberculosis_risk_index")
        context = {
            "country_code" : country_code ,
            "pincode" : pincode,
            "place_name" : place_name,
            "admin_name1" : admin_name1,
            "admin_name2" : admin_name2,
            "admin_name3" : admin_name3,
            "latitude" : latitude,
            "longitude" : longitude,
            "accuracy" : accuracy,
            "malaria_cause" : malaria_cause,
            "malaria_deaths" : malaria_deaths,
            "malnutrition_cause" : malnutrition_cause,
            "malnutrition_deaths" : malnutrition_deaths,
            "tuberculosis_cause" : tuberculosis_cause,
            "tuberculosis_deaths" : tuberculosis_deaths,
            "population" : population,
            "malaria_risk_factor" : malaria_risk_factor,
            "malnutrition_risk_factor" : malnutrition_risk_factor,
            "tuberculosis_risk_factor" : tuberculosis_risk_factor,
            "malaria_risk_index" : malaria_risk_index,
            "malnutrition_risk_index" : malnutrition_risk_index,
            "tuberculosis_risk_index" : tuberculosis_risk_index,

        }
        if latitude is not None and longitude is not None:
            template = "map/map.html"
        else:
            template = "map/error.html"
    return render(request,template,context)


def upload_data(request):
    with open("C:/Users/DeLL/Desktop/newcsv.csv") as f:
        for row in itertools.islice(csv.reader(f),30000,45000):
            print(row[0])
            obj, created = City.objects.get_or_create(
                id = row[0],
                country_code= row[1],
                pincode = int(row[2]),
                place_name = row[3],
                admin_name1 = row[4],
                admin_name2 = row[5],
                admin_name3 = row[6],
                latitude = float(row[7]),
                longitude = float(row[8]),
                accuracy = int(row[9]),
                malaria_cause = int(row[10]),
                malaria_deaths = int(row[11]),
                malnutrition_cause = int(row[12]),
                malnutrition_deaths = int(row[13]),
                tuberculosis_cause = int(row[14]),
                tuberculosis_deaths = int(row[15]),
                population = int(row[16]),
                malaria_risk_factor = float(row[17]),
                malnutrition_risk_factor = float(row[18]),
                tuberculosis_risk_factor = float(row[19]),
                malaria_risk_index = float(row[20]),
                malnutrition_risk_index = float(row[21]),
                tuberculosis_risk_index = float(row[22]),
            )
    context = {}
    return render(request, 'cityw/weather.html', context)
