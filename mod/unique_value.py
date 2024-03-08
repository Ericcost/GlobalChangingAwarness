def checking_unique_value(df):
    unique_values = [df[col].nunique() for col in df]
    for col, values in zip(df.columns, unique_values):
        print(f"Unique values in column '{col}': {values}")