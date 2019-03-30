from django.shortcuts import render

# Create your views here.
def onboarding(request):
    return render(request, 'userflow/index.html')



def experience(request):
    return None


def symptom_new(request):
    return None

def symptom_result(request):
    return None

def report(request):
    return None
