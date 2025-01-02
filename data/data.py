import pandas as pd

# This dataset has information about symptoms of various diseases
symptom_data = pd.read_csv('data/dataset.csv')

# This dataset has information about precautions for various diseases
precaution_data = pd.read_csv('data/precaution.csv')

print(symptom_data.head())
print(precaution_data.head())