
#Cafe Menu System#

print("Welcome to PY Restaurant")
Menu = {"Pizza" : 150,
        "Pasta" : 50,
        "Burger" : 99,
        "Tea" : 20,
        "Coffe": 40,
        "Chicken Lolipop": 399,

}
print("n\menu:")
for item, price in Menu.items():
    print(f"{item}: Rs {price}")

User_input =input("Enter the items of your order\n: ")
Items =[item.strip() for item in User_input.split(",")]

total_orders = 0
order_details= []

for item in Items:
    if item in Menu:
            
        
            qty = int(input(f"enter quantity: {item} :  "))
            item_total = Menu[item] * qty
            total_orders += item_total
            order_details.append((item, qty, item_total))
            print(f"🍔,🍵, 🍝,☕ {item} x {qty} added to your order (Rs {item_total})")
    else:
         print("Item Not Available")

print("Order Summary\n:")
for item, qty, item_total in order_details:
     print(f"{item}*{qty} = Rs {item_total}")

print("Total Bill = Rs",total_orders,)

    
            

