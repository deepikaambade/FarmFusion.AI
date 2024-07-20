Maharashtra Crop Recommendation System

This project implements a machine learning-based crop recommendation system for Maharashtra using various environmental and soil parameters.

   Dataset

The project uses a dataset named `mh_crop_final.csv` with the following columns:

- State: The state (Maharashtra in this case)
- District: District in Maharashtra
- Crop: The crop grown
- Season: The season in which the crop is grown
- Yield: Crop yield
- Soil Type: Type of soil
- Annual_Rainfall: Annual rainfall in mm
- Avg_Temperature: Average temperature in degrees Celsius
- Avg_Humidity: Average humidity in percentage
- Soil_pH: pH value of the soil

Sample data:
```
State,District,Crop,Season,Yield,Soil Type,Annual_Rainfall,Avg_Temperature,Avg_Humidity,Soil_pH
Maharashtra,AHMEDNAGAR,Arhar/Tur,Kharif,0.5,Coarse Soil,567.2,26.0,70.0,7.11
Maharashtra,AKOLA,Arhar/Tur,Kharif,2.27,Coarse Soil,779.5,27.5,65.0,7.14
Maharashtra,AMRAVATI,Arhar/Tur,Kharif,0.82,Coarse Soil,890.9,27.0,68.0,5.74
Maharashtra,AURANGABAD,Arhar/Tur,Kharif,0.77,Coarse Soil,715.4,26.5,72.0,7.35
Maharashtra,BEED,Arhar/Tur,Kharif,0.75,Coarse Soil,691.0,26.0,69.0,5.67
```

   Jupyter Notebook

The `code_crop.ipynb` notebook contains the code for:

1. Data loading and preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature encoding
4. Correlation analysis
5. Model training using:
   - XGBoost
   - Decision Tree
   - Ensemble model (XGBoost + Decision Tree)
6. Model evaluation and comparison
7. Cross-validation
8. Hyperparameter tuning for XGBoost

   Usage

1. Ensure you have all required libraries installed:
   ```
   pip install pandas numpy matplotlib seaborn sklearn xgboost imblearn
   ```

2. Place the `mh_crop_final.csv` file in the same directory as the notebook.

3. Open and run the `code_crop.ipynb` notebook in Jupyter or Google Colab.

   Key Features

- Handles class imbalance using RandomOverSampler
- Uses an ensemble model combining XGBoost and Decision Tree
- Performs cross-validation for model validation
- Includes hyperparameter tuning for XGBoost using GridSearchCV

   Results

The notebook outputs:
- Accuracy scores for individual models and the ensemble model
- Cross-validation scores for XGBoost
- Best parameters and accuracy from hyperparameter tuning

   Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.

   License

GPL 2.0
