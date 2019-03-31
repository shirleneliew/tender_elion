from django.shortcuts import render

# Create your views here.
def onboarding(request):
    return render(request, 'userflow/onboarding.html')

def experience(request):
    # process the get
    print(request.GET)

    mock = {
      'x_other_women': 514,
      'total_women': 5000,
      'days': [
        {'day': 1, 'pain': 3 },
        {'day': 2},
        {'day': 3, 'pain': 3 },
        {'day': 4, 'pain': 2 },
        {'day': 5, 'pain': 2 },
        {'day': 6 },
        {'day': 7, 'pain': 3, 'sore': 3 },
        {'day': 8 },
        {'day': 9 },
        {'day': 10, 'sore': 3 },
        {'day': 11, 'sore': 3 },
        {'day': 12},
        {'day': 13},
        {'day': 14, 'sore': 3},
        {'day': 15},
        {'day': 16},
        {'day': 17},
        {'day': 18},
        {'day': 19},
        {'day': 20},
        {'day': 21},
        {'day': 22, 'sore': 3},
        {'day': 23},
        {'day': 24},
        {'day': 25},
        {'day': 26},
        {'day': 27, 'sore': 5},
        {'day': 28,  'sore': 5},
        {'day': 29, 'pain': 5, 'sore': 5},
        {'day': 30, 'pain': 5, 'sore': 5}
      ]
    } 
    data = mock
    return render(request, 'userflow/experience.html', context=data)

def symptom_new(request):
    return render(request, 'userflow/symptom/new.html')

def symptom_result(request):
    data = {
        'results': [
            {
                'name': 'Cramp',
                'own': 2,
                'others': 4
            },
            {
                'name': 'Bloat',
                'own': 5,
                'others': 2
            }
        ]
    }
    return render(request, 'userflow/symptom/result.html', context=data)

def report(request):
    return render(request, 'userflow/report.html')
