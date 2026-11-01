# Self-Assessment Questions
# 1. The first bug I notcied was the missing ":". I found it simply throguht the traceback. I think I have a basic understanding of what needs to be done, but when the bug is not something specifically in the line or a syntax error, I struggle.
# 2. Apply the discount to the price that falls under the specific tier. It basically takes a price like 200 and puts it under the 'gold' tier which recieves a discoutn of 15%, causing the final price to be $170. A colleague most likely should be able to use it without reading the body.
# 3. I used AI to help me understand my bugs from the playback, and also asked for an explanation for me to understand.
# Exercise 1

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}") # Other option to do the SAME THING

# Exercise 2

# Define the function
def apply_discount(price, tier)
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise - Fixed Version with comments
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # makes sure loop takes number (stored in sale) and adds it to whatever your total currently is
print(f"Total: ${total}")

count = 0
for sale in sales:   # needed to add a semi-colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # Change to < (less than) makes the loop stop at 4, keeping me  safely inside the list.
    print(sales[i])
    i += 1
# Exercise 6

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)


