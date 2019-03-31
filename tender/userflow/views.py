from django.shortcuts import render

# Create your views here.
def onboarding(request):
    return render(request, 'userflow/onboarding.html')

def experience(request):
    return render(request, 'userflow/experience.html')

def symptom_new(request):
    return render(request, 'userflow/symptom/new.html')

def symptom_result(request):
    return render(request, 'userflow/symptom/result.html')

def report(request):
    return render(request, 'userflow/report.html')
