from django.shortcuts import render

# Create your views here.
def onboarding(request):
    return render(request, 'userflow/onboarding.html')

def experience(request):
    return render(request, 'userflow/experience.html')


def symptom_new(request):
    return None

def symptom_result(request):
    return None

def report(request):
    return None
