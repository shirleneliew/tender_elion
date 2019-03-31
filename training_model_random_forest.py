# Step 1, import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Import dataset
model_df = pd.read_pickle("data/processed_symptoms.pkl")

# Step 2, create predictor and target variables

X_cramp = model_df[['acne','backache', 'bloating', 'diarrhea', 'dizzy', 'headache', 'mood', 'nausea', 'sore', 'cycle_percentage']]
y_cramp = model_df.cramp.values

X_bloating = model_df[['acne','backache', 'cramp', 'diarrhea', 'dizzy', 'headache', 'mood', 'nausea', 'sore', 'cycle_percentage']]
y_bloating = model_df.bloating.values

X_mood = model_df[['acne','backache', 'bloating', 'diarrhea', 'dizzy', 'headache', 'cramp', 'nausea', 'sore', 'cycle_percentage']]
y_mood = model_df.mood.values

# Step 5a, create a random forest regressor with the best parameters
rfr = RandomForestRegressor(max_depth=20, 
                            n_estimators=200,                               
                            random_state=42, 
                            verbose=True)

# Step 6, create predictions using model

# Create splits for cramps
X_train_cramp, X_test_cramp, y_train_cramp, y_test_cramp = train_test_split(X_cramp, y_cramp, test_size=0.2)

# Create splits for bloating
X_train_bloating, X_test_bloating, y_train_bloating, y_test_bloating = train_test_split(X_bloating, y_bloating, test_size=0.2)

# Create splits for mood
X_train_mood, X_test_mood, y_train_mood, y_test_mood = train_test_split(X_mood, y_mood, test_size=0.2)

# Fit models
rfr.fit(X_train_cramp, y_train_cramp)
rfr.fit(X_train_bloating, y_train_bloating)
rfr.fit(X_train_mood, y_train_mood)

# Make predictions
def predict_cramps(X): # This should be 9 values between 0 and 100, and a 10th value between 0 and 1
    y_pred = rfr.predict(X)
    print(y_pred)
    return y_pred

def predict_bloating(X):
    y_pred = rfr.predict(X)
    print(y_pred)
    return y_pred

def predict_mood(X):
    y_pred = rfr.predict(X)
    print(y_pred)
    return y_pred