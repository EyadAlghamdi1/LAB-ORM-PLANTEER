from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Plant

# Create your views here.
def detail_view(request:HttpRequest,plant_id:int):
    plant_detail = Plant.objects.get(pk=plant_id)
    featured_plants = Plant.objects.all()[:3]
    return render(request,"plant/detail.html", {"plant_detail":plant_detail ,'featured_plants': featured_plants })

def all_view(request:HttpRequest):
    plants = Plant.objects.all()
    return render(request,"plant/all_plants.html",{"plants": plants})

def update_view(request:HttpRequest,plant_id:int):
    plant_detail = Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        plant_detail.name = request.POST["name"]
        plant_detail.about = request.POST["about"]
        plant_detail.used_for = request.POST["used_for"]
        plant_detail.image = request.FILES["image"]
        plant_detail.category = request.POST["category"]
        plant_detail.is_edible = request.POST["is_edible"]
        plant_detail.save()
    return render(request,"plant/update.html", {"plant_detail":plant_detail} )

def delete_view(request:HttpRequest,plant_id:int):
    plant_detail = Plant.objects.get(pk=plant_id)
    plant_detail.delete()
    return render(request,"plant/all_plants.html")

def search_view(request: HttpRequest):
    word = request.GET.get('word', '')  
    results = Plant.objects.filter(name__icontains=word)
    return render(request,"plant/search.html", {'results': results, 'word': word})



def add_view(request:HttpRequest):
    if request.method == "POST":
        new_plant = Plant(

        name=request.POST["name"],
        about = request.POST["about"],
        used_for = request.POST["used_for"],
        image = request.FILES["image"],
        category = request.POST["category"],
        is_edible = request.POST["is_edible"]
 
        )
        new_plant.save()
    return render(request,"plant/add_new_plant.html")