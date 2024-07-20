Crop Recommendation System

This project implements a machine learning-based crop recommendation system using various environmental and soil parameters.

   Dataset

The project uses a dataset named `crop_recommendation.csv` with the following columns:

- N: Nitrogen content in the soil
- P: Phosphorus content in the soil
- K: Potassium content in the soil
- temperature: Temperature in degree Celsius
- humidity: Relative humidity in %
- ph: pH value of the soil
- rainfall: Rainfall in mm
- label: The recommended crop for given conditions

Sample data:
```
N,P,K,temperature,humidity,ph,rainfall,label
90,42,43,20.87974372,82.00274424,6.502985292,202.9355362,rice
85,58,41,21.77046169,80.31964409,7.038096361,226.6555374,rice
60,55,44,23.00445915,82.32076297,7.840207144,263.9642476,rice
74,35,40,26.49109635,80.15836264,6.980400905,242.8640342,rice
78,42,42,20.13017482,81.60487287,7.628472891,262.7173405,rice
```

   Model

The `crop_recommendation_model` script contains the code for:

1. Data preprocessing
2. Exploratory Data Analysis (EDA)
3. Model training using various algorithms:
   - Decision Tree
   - Naive Bayes
   - Support Vector Machine (SVM)
   - Logistic Regression
   - Random Forest
   - XGBoost
4. Model evaluation and comparison
5. Saving trained models

   Usage

1. Ensure you have all required libraries installed:
   ```
   pip install pandas numpy matplotlib seaborn sklearn xgboost
   ```

2. Place the `crop_recommendation.csv` file in the same directory as the script.

3. Run the `crop_recommendation_model` script to train and evaluate the models.

4. The script will output accuracy comparisons and save the trained models as pickle files.

   Making Predictions

After training, you can use the saved models to make predictions. For example:

```python
import pickle

  Load the model
with open('RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

  Make a prediction
data = np.array([[104, 18, 30, 23.603016, 60.3, 6.7, 140.91]])
prediction = model.predict(data)
print(prediction)
```

   Results

![image](https://github.com/user-attachments/assets/c4f0b898-94ba-46c0-85c4-062fee145105)
Decision Tree --> 0.9
Naive Bayes --> 0.990909090909091
SVM --> 0.9795454545454545
Logistic Regression --> 0.9522727272727273
RF --> 0.990909090909091
XGBoost --> 0.990909090909091


   Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.

   License

GPL 2.0
