import requests
import pandas as pd
import os

# make sure output folder exists
os.makedirs("output", exist_ok=True)

# function to get data and save as CSV
def fetch_to_csv(url, filename):
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv(f"output/{filename}", index=False)
    print(f"✅ Saved {filename} ({len(df)} rows)")

# main
if __name__ == "__main__":
    fetch_to_csv("https://fakestoreapi.com/products", "products.csv")
    fetch_to_csv("https://fakestoreapi.com/users", "users.csv")
    fetch_to_csv("https://fakestoreapi.com/carts", "orders.csv")
