from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from datetime import timedelta

df = pd.read_pickle('userflow/processed_symptoms.pkl')


def get_distribution(cl, pl):
    similar_people = df[
        (df.cycle_length_initial >= timedelta(days=cl - 1)) &
        (df.cycle_length_initial <= timedelta(days=cl + 1)) &
        (df.period_length_initial >= timedelta(days=pl - 1)) &
        (df.period_length_initial <= timedelta(days=pl + 1))
    ]
    return similar_people


def test(request):
    # return df[df.cycle]
    ss = get_distribution(26, 4)
    return HttpResponse(ss.shape[0])


# Create your views here.
def onboarding(request):
    return render(request, 'userflow/onboarding.html')


def experience(request):
    # process the get
    print(request.GET)
    period_length = request.GET.get('period_length')
    cycle_length = request.GET.get('cycle_length')

    mock = {
        'x_other_women': 1234,
        'total_women': 6729,
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
