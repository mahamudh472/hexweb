from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def partnership(request):
    return render(request, 'partnership.html')
def risk_map(request):
    return render(request, 'risk-map.html')
def travel_hub(request):
    return render(request, 'travel-hub.html')

