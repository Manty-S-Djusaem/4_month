from django.shortcuts import render, HttpResponse
from .models import Vegetables


# Create your views here.
def homepage(request):
    products = Vegetables.object.all()    #list
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context)


def pomidor(request):
    pomidor_object = Vegetables.object.get(id=1)
    description = pomidor_object.description
    return HttpResponse(description)
