import pandas as pd
import requests

def get_exchange_rates():
    url = "https://api.frankfurter.app/latest?from=GBP&to=USD,INR"
    response = requests.get(url)
    data = response.json()

    if "rates" not in data:
        raise ValueError(f"Exchange rate API error: {data}")

    return data["rates"]

def transform_data(input_path="./data/raw/data.csv", output_path="./data/processed/cleaned_data.csv"):
    df = pd.read_csv(input_path)

    # Drop missing values
    df.dropna(subset=["CustomerID"], inplace=True)

    # Add revenue in GBP
    df["Revenue_GBP"] = df["Quantity"] * df["UnitPrice"]

    # Fetch exchange rates
    rates = get_exchange_rates()

    # Enrich with converted revenue
    df["Revenue_USD"] = df["Revenue_GBP"] * rates["USD"]
    df["Revenue_INR"] = df["Revenue_GBP"] * rates["INR"]

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print(f"Data cleaned, enriched with exchange rates, and saved to {output_path}")
    return df, rates
