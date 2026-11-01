# Reflection Questions

# What is the most surprising thing about how lists work in Python compared to what you expected coming in?
# One thing that I found suprising about Python lists is that they are more dynamic and can hold mixed type datas than rigid arrays.
# Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
# In my advanced accounting classes, where I may be asekd to analyze financial statements manually. I could use a Python list to store the ledger data and instatntly automate the calculations and categorization.


print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


print("--- Exercise 2: Index Practice ---")

print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last itme

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)


print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs first three items
print(inventory[-2:]) # grabs last two items
print(inventory[::2]) 


print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
inventory.appen("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)


print("--- Exercise 5: Tuple Comparison ---")

coords = (40.7128, -74.0060) # New York City coordinates

try:
    coords[0] = 99  # This will raise a TypeError because tuples are 
expect TypeError as error:
    print(f"TypeError caught:{error}")
    print("Tuples protect coordinates from being changed by accident")


print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f" Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for sale in sales:
    if sale > best:
        best = amount
    if sale < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")


print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount

print(prices)
print(discounted)


print("--- Exercise 8: Filter ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Aberage: {sum(high_sales) / len(high_sales):.2f}")