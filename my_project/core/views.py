from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, people, Customer
from django.views.decorators.csrf import csrf_exempt
# from django.authantication.decorators import login_required
def home(request):
    return HttpResponse("<h1>Hello, world!</h1><p>Welcome to my Django project.</p>")
def about(request):
    return render(request, 'core/index.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        # Here you can handle the form data, e.g., save it to the database or send an email
        # return HttpResponse(f"Thank you, {name}! Your message has been received.")
        Person.objects.create(
        name=name,
        email=email,
        address=address
        )
        return redirect('home')  # Redirect to the home page after form submission
    return render(request, "persnoal/index.html")
def about(request):
    # return render(request, 'core/index.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        people.objects.create(
        name=name,
        email=email,
        age=age,
        address=address
        )
        return redirect('home')  # Redirect to the home page after form submission
    return render(request, "core/index.html")
def Customerr(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        cinc = request.POST.get('cinc')
        Customer.objects.create(
        name=name,
        email=email,
        age=age,
        address=address,
        salary=salary,
        cinc=cinc
        )
        return redirect('home')
    Customeer = Customer.objects.all()
    return render(request, "Customer/Customer.html",{'Customeer':Customeer})