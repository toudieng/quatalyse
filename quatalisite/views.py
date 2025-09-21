from django.shortcuts import render

def home(request):
    valeurs = ["Rigueur", "Créativité", "Intégrité", "Confidentialité", "Cohésion d’équipe"]
    return render(request, 'home.html', {'valeurs': valeurs})


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def formations(request):
    return render(request, 'formations.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
