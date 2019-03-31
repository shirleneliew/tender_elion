School of AI Health Hackathon submission -- Singapore!
Team 14
 
# psloveyoutoo
Empowering women to take charge of their reproductive health.

See our presentation [here](https://docs.google.com/presentation/d/1d_gJzHZWGnPXRoLjxYsFEVm_Z2fMSVxz09TjiEebByw/edit?usp=sharing).

## \#WomensHealth
Stigma surrounding menstrual health hinders women from talking about their menstrual health openly and this has a negative impact on women seeking the necessary help to manage their menstrual health. A survey done by Public Health England revealed that 35% of women have experienced heavy menstrual bleeding, which previous evidence shows is associated with higher unemployment and absence from work.Survey also shows that less than half of women seeking help for their symptoms, regardless of severity.

## \#EmpoweredIsTheNewPink
<b>psloveyoutoo</b> is created with the idea to overcome this stigma and empower women to understand and manage their menstrual health. It provides the solution to the isolation and lack of information which women are currently facing - with the power of machine learning: we connect the pslove dataset with what the user is feeling now, in an intuitive and appealing interface.

## \#NotJustAnotherPeriodTracker
In the current consumer digital app space, there are various other menstrual cycle tracking apps - most are ‘input based’ which is used by individual to track their period and predict fertile period. What differentiates <b>psloveyoutoo</b> from these other apps is that in the <b>psloveyoutoo</b> app, inputs from user will be coupled with outputs by the app. Using dataset obtained from the <b>psloveyoutoo</b> database, we can match individuals to a subset of users and the individual is able to see what other “women like me” also experiences during their menstrual cycle.

## \#ManageYourHealth
In addition, the data input categories are designed to guide women to record accurate health information which will be of value to clinicians should the user decide to consult a doctor. 

# How to view code

### App
To run the app locally
1. clone the repo, install the requirements from requirements.txt
2. change dir to /tender to  
3. run 'python manage.py runserver'

To experience the app, go to:
[periodlove](https://periodlove.herokuapp.com/onboarding).

The app is not yet connected to the model.

### Model and data cleaning
Model libraries are in the 'model' folder. Training script can be opened from training_model_random_forest.py.

The jupyter notebooks to clean the code and create the model can be found in the 'data_cleaning' folder.
Run 'model_final.ipynb' to see explanation of our data cleaning and model.
To run the notebooks, please put the original pslove csv files in the 'data_cleaning' folder.


