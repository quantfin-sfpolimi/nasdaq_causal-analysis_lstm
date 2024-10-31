import pandas as pd
import pickle

# Carica i DataFrame dai file pickle
with open('pickle_files/nasdaq_dataframe.pkl', 'rb') as f:
    nasdaq_dataframe = pickle.load(f)

with open('pickle_files/cleaned_nasdaq_dataframe.pkl', 'rb') as f:
    cleaned_nasdaq_dataframe = pickle.load(f)

# 1. Controllo dei valori nulli
print("Valori nulli in nasdaq_dataframe:\n", nasdaq_dataframe.isnull().sum())
print("\nValori nulli in cleaned_nasdaq_dataframe:\n", cleaned_nasdaq_dataframe.isnull().sum())

# 2. Dimensioni dei DataFrame
print("\nDimensioni originali:", nasdaq_dataframe.shape)
print("Dimensioni pulite:", cleaned_nasdaq_dataframe.shape)

# 3. Controllo duplicati
print("\nDuplicati in nasdaq_dataframe:", nasdaq_dataframe.duplicated().sum())
print("Duplicati in cleaned_nasdaq_dataframe:", cleaned_nasdaq_dataframe.duplicated().sum())

# 4. Statistiche descrittive per rilevare potenziali outlier
print("\nStatistiche descrittive di nasdaq_dataframe:\n", nasdaq_dataframe.describe())
print("\nStatistiche descrittive di cleaned_nasdaq_dataframe:\n", cleaned_nasdaq_dataframe.describe())
