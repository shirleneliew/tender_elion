from django.shortcuts import render

# Create your views here.
def onboarding(request):
    return render(request, 'userflow/onboarding.html')

def experience(request):
    # process the get
    print(request.GET)

    mock = {
      'x_other_women': 1234,
      'total_women': 5000,
      1: {'pain': 3, 'soreness': 6},
      10: {'soreness': 8}
    } 
    data = mock
    return render(request, 'userflow/experience.html', context=data)

def symptom_new(request):
    return render(request, 'userflow/symptom/new.html')

def symptom_result(request):
    return render(request, 'userflow/symptom/result.html')

def report(request):
    return render(request, 'userflow/report.html')
