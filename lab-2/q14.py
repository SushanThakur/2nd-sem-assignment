products = {"Apple": 100, "Banana": 50, "Orange": 80}

# a. Add product
products["Mango"] = 120

# b. Update price
products["Apple"] = 110

# c. Find products within price range
min_price = 60
max_price = 100
for product, price in products.items():
    if min_price <= price <= max_price:
        print(product, price)

