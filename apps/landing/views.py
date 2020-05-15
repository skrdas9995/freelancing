from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "landing/index-logged-out.html" )

def aboutus(request):
    return render(request, "landing/single-company-profile-OpenStreetMap.html" )

def priceplan(request):
    return render(request, "landing/pages-pricing-plans.html" )

def contact(request):
    return render(request, "pages-contact-OpenStreetMap.html" )

def blog(request):
    return render(request, "pages-blog.html" )
