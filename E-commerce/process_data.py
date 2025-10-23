import pandas as pd
import ast
import os

os.makedirs("output", exist_ok=True)

# Load data
products = pd.read_csv("output/products.csv")
orders = pd.read_csv("output/orders.csv")
users = pd.read_csv("output/users.csv")

# Parse products in orders
def parse_products(cell):
    try:
        return ast.literal_eval(cell)
    except:
        return []

orders["products_parsed"] = orders["products"].apply(parse_products)

rows = []
for _, order in orders.iterrows():
    user_id = order["userId"]
    for p in order["products_parsed"]:
        rows.append({
            "user_id": user_id,
            "product_id": p["productId"],
            "quantity": p["quantity"]
        })

df_orders = pd.DataFrame(rows)
df = df_orders.merge(products, left_on="product_id", right_on="id", how="left")
df["revenue"] = df["price"] * df["quantity"]
df.to_csv("output/orders_final.csv", index=False)
print("✅ Saved orders_final.csv")
