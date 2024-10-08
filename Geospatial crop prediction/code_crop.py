
Original file is located at
    https://colab.research.google.com/drive/1GWUohOEPiavlrJ2UqP7GcfMDx-2XvOqH

Importing files
"""

import pandas as pd

df = pd.read_csv("mh_crop_final.csv", na_values="No data")

df

df.head()

df.isna().sum()

"""Dropping Unnecessary columns and rows which has null values. In this case, its "State"."""

df=df.dropna()

df.drop(columns=["State"], inplace=True)

df.isna().sum()

"""Label encoding for categorical columns after checking dtypes"""

df.dtypes

df

df['Season'].unique()

# Create a LabelEncoder object
le = LabelEncoder()

# Label encode categorical columns, except for 'Crop'
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

df.dtypes

df.loc[:, 'District'] = le.fit_transform(df['District'])
df.dtypes

df.dtypes



# Calculate the correlation matrix
corr = df.corr()
threshold = 0.3

# Print strong correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            print(f"Strong correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

# Print strong negative correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if corr.iloc[i, j] < -threshold:
            print(f"Strong negative correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

import pandas as pd # Import pandas for data manipulation

# Assuming 'df' is your DataFrame containing the data
corr = df.corr()  # Calculate the correlation matrix and store it in 'corr'

# Set the threshold for strong correlations
threshold = 0.3

# Iterate over the correlation matrix and print pairs with strong correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            print(f"Strong correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

# Iterate over the correlation matrix and print pairs with strong negative correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if corr.iloc[i, j] < -threshold:
            print(f"Strong negative correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


# Label encode the target column 'Crop'
df['Crop'] = le.fit_transform(df['Crop'])

# Encode 'District' column
df['District'] = le.fit_transform(df['District'])

# Display the data types of the dataframe
print(df.dtypes)

# Calculate the correlation matrix
corr = df.corr()
threshold = 0.3

# Print strong correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            print(f"Strong correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

# Print strong negative correlations
for i in range(len(corr.columns)):
    for j in range(i):
        if corr.iloc[i, j] < -threshold:
            print(f"Strong negative correlation between {corr.columns[i]} and {corr.columns[j]}: {corr.iloc[i, j]}")

# Split the data into features and target
X = df.drop('Crop', axis=1)
y = df['Crop']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check for class imbalance
class_counts = df['Crop'].value_counts()
is_balanced = class_counts.min() / class_counts.max() >= 0.8
print(f"Is the dataset balanced? {is_balanced}")

# If imbalanced, apply oversampling
if not is_balanced:
    oversampler = RandomOverSampler(random_state=143)
    X_resampled, y_resampled = oversampler.fit_resample(X, y)
else:
    X_resampled, y_resampled = X, y

# Initialize the individual models
xgb_model = XGBClassifier()
dt_model = DecisionTreeClassifier()

# Create the VotingClassifier
ensemble_model = VotingClassifier(estimators=[('xgb', xgb_model), ('dt', dt_model)], voting='hard')

# Fit the ensemble model on the resampled training data
ensemble_model.fit(X_resampled, y_resampled)

# Make predictions on the test data
y_pred_ensemble = ensemble_model.predict(X_test)

# Evaluate the ensemble model
accuracy_ensemble = accuracy_score(y_test, y_pred_ensemble)
print(f"Ensemble Model (XGBoost + Decision Tree): {accuracy_ensemble:.4f}")

# Evaluate individual models for comparison
xgb_model.fit(X_resampled, y_resampled)
y_pred_xgb = xgb_model.predict(X_test)
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
print(f"XGBoost: {accuracy_xgb:.4f}")

dt_model.fit(X_resampled, y_resampled)
y_pred_dt = dt_model.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree: {accuracy_dt:.4f}")

# Perform cross-validation for XGBoost
xgb_cv_scores = cross_val_score(xgb_model, X_resampled, y_resampled, cv=5)
print(f"XGBoost Cross-Validation Scores: {xgb_cv_scores}")
print(f"Mean XGBoost CV Accuracy: {xgb_cv_scores.mean():.4f}")

# Hyperparameter tuning for XGBoost using GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.1, 0.01, 0.001]
}

grid_search = GridSearchCV(estimator=XGBClassifier(), param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_resampled, y_resampled)

print("Best parameters found: ", grid_search.best_params_)
print("Best accuracy found: ", grid_search.best_score_)
