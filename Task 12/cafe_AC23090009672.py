# calculates the total value of a given stock and prints it
# Menu items, their current stock and their price
menu = ["coffee", "tea", "cake", "sandwich"]
stock = {"coffee": 5, "tea": 8, "cake": 4, "sandwich": 12}
price = {"coffee": 2.5, "tea": 1.80, "cake": 2, "sandwich": 3}

stock_values = list(stock.values())
price_values = list(price.values())

# Iterates through the menu and calculates current stock value
total_stock = 0
for item in menu:
    stock_value = stock.get(item)
    price_value = price.get(item)
    total_stock += stock_value * price_value

print(total_stock)
    