import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder# File paths
file_path = r"C:\Users\owner\OneDrive\Desktop\AI ASSISTED CODING\Lab 17.4\financial_data.csv"
output_path = r"C:\Users\owner\OneDrive\Desktop\AI ASSISTED CODING\Lab 17.4\engineered_financial_data.csv"

if not os.path.exists(file_path):
    sample_data = {
        "date": pd.date_range(start="2024-01-01", periods=60),
        "company_name": ["ABC Corp", "XYZ Ltd", "LMN Inc", "ABC Corp", "XYZ Ltd"] * 12,
        "sector": ["Tech", "Finance", "Retail", "Tech", "Finance"] * 12,
        "stock_price": np.random.uniform(100, 500, 60),
        "volume": np.random.randint(1000, 5000, 60)
    }
    df = pd.DataFrame(sample_data)
    df.loc[5, 'stock_price'] = np.nan
    df.loc[10, 'volume'] = np.nan
    df.to_csv(file_path, index=False)
    print(f"📁 Sample financial dataset created at: {file_path}")
df = pd.read_csv(file_path)
df['stock_price'].fillna(df['stock_price'].mean(), inplace=True)
df['volume'].fillna(df['volume'].mean(), inplace=True)
df['MA_7'] = df['stock_price'].rolling(window=7, min_periods=1).mean()
df['MA_30'] = df['stock_price'].rolling(window=30, min_periods=1).mean()
scaler = StandardScaler()
df[['stock_price', 'volume', 'MA_7', 'MA_30']] = scaler.fit_transform(df[['stock_price', 'volume', 'MA_7', 'MA_30']])
label_encoders = {}
for col in ['sector', 'company_name']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le# Save the feature-engineered dataset
df.to_csv(output_path, index=False)
print(f"✅ Feature-engineered dataset saved successfully at: {output_path}")

