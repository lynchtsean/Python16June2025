subtotal = 0
items = []

num_items = int(input("How many items do you want to buy? "))

for i in range(num_items):
    name = input(f"\nEnter name of item {i + 1}: ")
    price = float(input(f"Enter price of {name}: "))
    quantity = int(input(f"Enter quantity of {name}: "))
    
    total = price * quantity
    subtotal += total
    items.append((name, quantity, total))

discount = subtotal * 0.10
tax = (subtotal - discount) * 0.05
total = subtotal - discount + tax

print("\nReceipt:")
for name, qty, total_price in items:
    print(f"- {name} x{qty} = ${total_price:.2f}")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")