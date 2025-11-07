import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder# --- 1. Create Simulated Data (Replace with pd.read_csv('your_file.csv') later) ---
data = {
    'id': range(101, 111),
    'salary': [60000, np.nan, 75000, 55000, 120000, np.nan, 65000, 90000, np.nan, 85000],
    'department': ['HR', 'Tech', 'hr', 'Sales', 'Technology', 'FINANCE', np.nan, 'sales', 'Finance', 'Human Resources'],
    'job_role': ['Manager', 'Developer', 'Analyst', 'Associate', 'Lead', 'Manager', 'Analyst', 'Associate', 'Developer', 'Lead'],
    'joining_date': ['2020-01-15', '2021/05/20', '2019-11-01', '2022-03-10', '2018-09-25', '2023-01-05', '04-18-2021', np.nan, '2019/03/15', '2022-02-14']
}
df = pd.DataFrame(data)

print("--- Original Data Info ---")
df.info()
mean_salary = df['salary'].mean()
df['salary'].fillna(mean_salary, inplace=True)
df['department'].fillna('Unknown', inplace=True) # Fill missing department
df['joining_date'].fillna(df['joining_date'].mode()[0], inplace=True) # Fill missing date with mode
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')
df['department'] = df['department'].str.lower()
department_map = {
    'hr': 'HR',
    'human resources': 'HR',
    'tech': 'Technology',
    'technology': 'Technology',
    'sales': 'Sales',
    'finance': 'Finance',
    'unknown': 'Unknown'
}
df['department'] = df['department'].replace(department_map)
le = LabelEncoder()
df['department_encoded'] = le.fit_transform(df['department'])
df['job_role_encoded'] = le.fit_transform(df['job_role'])
print("\n" * 2)
print("--- Cleaned and Preprocessed DataFrame Head ---")
print(df[['salary', 'department', 'joining_date', 'department_encoded', 'job_role_encoded']].head())
print("\n--- Cleaned Data Info (Verify Datatypes) ---")
df.info()