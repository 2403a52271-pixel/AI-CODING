import pandas as pd
import numpy as np
import os
file_path = r"C:\Users\owner\OneDrive\Desktop\AI ASSISTED CODING\Lab 17.4\healthcare_data.csv"
if not os.path.exists(file_path):
    print("⚠️ File not found — creating a sample healthcare_data.csv file for testing...")
    sample_data = {
        'patient_id': [1, 2, 3, 4],
        'gender': ['M', 'male', 'F', 'female'],
        'height': [170, 165, 160, np.nan],
        'blood_pressure': [120, np.nan, 110, 130],
        'heart_rate': [80, 78, np.nan, 85]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(file_path, index=False)
    print("✅ Sample file created successfully!\n")
df = pd.read_csv(file_path)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.mean()))

if 'height' in df.columns:
    df['height'] = df['height'].apply(lambda x: x / 100 if pd.notnull(x) else x)

if 'gender' in df.columns:
    df['gender'] = (
        df['gender']
        .astype(str)
        .str.strip()
        .str.lower()
        .replace({'m': 'Male', 'male': 'Male', 'f': 'Female', 'female': 'Female'})
    )

if 'patient_id' in df.columns:
    df.drop(columns='patient_id', inplace=True)

output_file = "cleaned_healthcare_data.csv"
df.to_csv(output_file, index=False)

print("\n✅ Healthcare dataset cleaned successfully!")
print("📁 Cleaned dataset saved as:", output_file)
print("\n🧾 Cleaned Data Preview:\n")
print(df.head())
