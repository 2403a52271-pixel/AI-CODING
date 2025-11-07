import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Create Sample Data
data = {
    'transaction_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'transaction_date': ['2023-01-15', '2023/01/22', '16-FEB-2023', '2023-03-01',
                         '2023-04-10', '2023-05-05', '2023-06-20', '2023-07-07'],
    'product_category': ['Electronics', 'Apparel', 'Electronics', 'Home Goods',
                         'Apparel', 'Home Goods', 'Electronics', 'Apparel'],
    'transaction_amount': [150.50, 45.00, -10.00, 75.99, 200.00, 0.00, 350.75, 55.25],
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8]
}

df = pd.DataFrame(data)


df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce', format='mixed')


df['Month-Year'] = df['transaction_date'].dt.to_period('M').astype(str)


df = df[df['transaction_amount'] > 0]


scaler = MinMaxScaler()
df['transaction_amount_normalized'] = scaler.fit_transform(df[['transaction_amount']])


print(df[['transaction_id', 'transaction_date', 'Month-Year',
          'transaction_amount', 'transaction_amount_normalized']])