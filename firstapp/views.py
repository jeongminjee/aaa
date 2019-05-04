from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def recom_food(request):
    return render(request,'recm_food.html')
def presient(request):
    return render(request,'president.html')
def challenge(request):
    return render(request,'challenge.html')