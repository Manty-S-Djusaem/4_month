from django.shortcuts import render, HttpResponse
from .models import PC
from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    template_name = "example.html"


def homepage(request):
    return render(request, "index.html")


def personal_computer(request):
    laptop_object = PC.objects.get(id=1)
    description = f"{laptop_object.name}, {laptop_object.description}"
    return HttpResponse(description)


def categories(request):
    products = PC.objects.all()
    data = {"all_laptops": products}
    return render(request, "categories.html", context=data)
# def categories_view(request):
#     return HttpResponse("<h1>Список Категорий")

# from django.shortcuts import render, HttpResponse
# from .models import PC
# from django.views.generic import TemplateView
#
#
# # Create your views here.
# class ExampleView(TemplateView):
#     template_name = "index.html"
#
#
# def about(request):
#     return render(request, 'index.html')
#
#
# def homepage(request):
#     # SELECT * FROM Vegetables
#     products = PC.objects.all()  # list
#     context = {"all_vegetables": products}
#     return render(request, "product_list.html", context)
#
#
# def personal_computer(request):
#     laptop_object = PC.objects.get(id=1)
#     description = f"{laptop_object.name}, {laptop_object.description}"
#     return HttpResponse(description)
#
#
# def categories_view(request):
#     categories = PC.objects.all()
#     c = {"categories": categories}
#     return render(request, "categories.html", c)
# # def categories_view(request):
# #     return HttpResponse("<h1>Список Категорий")

