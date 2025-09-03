import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def run_pipeline(input_file, output_file):
    df = pd.read_csv(input_file)
    df.fillna(method='ffill', inplace=True)
    df['Category'] = df['Category'].astype('category').cat.codes
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    df['Expense_Type'] = df['Amount'].apply(lambda x: 'High' if x > 1000 else 'Low')
    scaler = MinMaxScaler()
    df[['Amount']] = scaler.fit_transform(df[['Amount']])
    df.to_csv(output_file, index=False)
    print("Pipeline executed successfully!")

