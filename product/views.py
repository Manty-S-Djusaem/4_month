from django.shortcuts import render, HttpResponse
from .models import PC
from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"


class HyperText(TemplateView):
    template_name = "hypertext.html"


class Web_List(TemplateView):
    template_name = "Web_List.html"


class Browser(TemplateView):
    template_name = "Browser.html"


class HTTP(TemplateView):
    template_name = "HTTP.html"


class HTTPS(TemplateView):
    template_name = "HTTPS.html"

class RazerBlade15(TemplateView):
    template_name = "RazerBlade15.html"

class AsusROGZephyrusG14(TemplateView):
    template_name = "AsusROGZephyrusG14.html"

class LenovoLegion5Pro(TemplateView):
    template_name = "LenovoLegion5Pro.html"

class RazerBlade14(TemplateView):
    template_name = "RazerBlade14.html"

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

def pc_detail(request, id):
    pc = Pc.objects.get(id=id)
    context = {"pc": pc}
    return render(request, "product/pc_info.html", context)


# def categories_view(request):
#     return HttpResponse("<h1>Список Категорий")

# from django.shortcuts import render, HttpResponse
# from django.views.generic import TemplateView
# from .models import PC, Categories
#
#
# class AboutView(TemplateView):
#     template_name = "about.html"
#
#
# def about(request):
#     return render(request, 'about.html')
#
#
# # Create your views here.
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
# def categories(request):
#     products = Categories.objects.all()
#     data = {"all_laptops": products}
#     return render(request, "categories.html", context=data)


# def categories_view(request):
#     return HttpResponse("<h1>Список Категорий")


# from django.shortcuts import render, HttpResponse
# from .models import PC
# from django.views.generic import TemplateView
#
#
# # Create your views here.
# class AboutView(TemplateView):
#     template_name = "exampld.html"
#
#
# def homepage(request):
#     return render(request, "index.html")
#
#
# def personal_computer(request):
#     laptop_object = PC.objects.get(id=1)
#     description = f"{laptop_object.name}, {laptop_object.description}"
#     return HttpResponse(description)
#
#
# def categories(request):
#     products = PC.objects.all()
#     data = {"all_laptops": products}
#     return render(request, "categories.html", context=data)
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

# def example():
#     return None
