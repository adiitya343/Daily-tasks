print("Welcome to the WENDY'S Resto!")
print("")
print("Available Courses:")
print("Starters \nMain course \nDessert")
print("")

# Dish names and prices as individual variables
starter1, starter1_price = "Paneer Tikka", 139
starter2, starter2_price = "Veg Crispy", 149
starter3, starter3_price = "Harabhara Kebab", 199

main1, main1_price = "Dal Tadka", 129
main2, main2_price = "Thai Curry", 299
main3, main3_price = "Veg Kholapuri", 149
main4, main4_price = "Biryani", 349

dessert1, dessert1_price = "Vanilla IceCream", 99
dessert2, dessert2_price = "Falooda", 149
dessert3, dessert3_price = "Sizzling Brownie", 219

orderlist = {}

def print_menu(cuisine):
    if cuisine == "starters":
        print(f"{starter1} ({starter1_price})")
        print(f"{starter2} ({starter2_price})")
        print(f"{starter3} ({starter3_price})")
    elif cuisine == "main course":
        print(f"{main1} ({main1_price})")
        print(f"{main2} ({main2_price})")
        print(f"{main3} ({main3_price})")
        print(f"{main4} ({main4_price})")
    elif cuisine == "dessert":
        print(f"{dessert1} ({dessert1_price})")
        print(f"{dessert2} ({dessert2_price})")
        print(f"{dessert3} ({dessert3_price})")

while True:
    print("\nAvailable Courses: Starters, Main Course, Dessert")
    cuisine = input("Enter your choice or type 'Done' to finish ordering: ").strip().lower()

    if cuisine == "done":
        break

    if cuisine in ["starters", "main course", "dessert"]:
        print("\nSelect your food from the menu:")
        print_menu(cuisine)

        while True:
            order = input("Enter your dish or type 'Back' to return to the menu: ").strip()
            if order.lower() == "back":
                break

            if (cuisine == "starters" and order in [starter1, starter2, starter3]) or \
               (cuisine == "main course" and order in [main1, main2, main3, main4]) or \
               (cuisine == "dessert" and order in [dessert1, dessert2, dessert3]):
                quantity = input(f"Enter the quantity for {order}: ").strip()
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity. Please enter a positive number.")
                    continue
                quantity = int(quantity)
                if order in orderlist:
                    orderlist[order]['quantity'] += quantity
                else:
                    price = eval(f"{order.replace(' ', '').lower()}_price")
                    orderlist[order] = {'price': price, 'quantity': quantity}
                print(f"{quantity} x {order} added to your order.")
            else:
                print("Invalid dish. Please choose from the menu.")
    else:
        print("Invalid choice! Please select Starters, Main Course, Dessert, or type 'Done' to finish.")

# Billing process
bill = 0
print("\nYour Order:")
print("Dish\t\t\tQuantity\tPrice")
print("----------------------------------------")
for dish, details in orderlist.items():
    dish_total = details['price'] * details['quantity']
    bill += dish_total
    print(f"{dish}\t\t{details['quantity']}\t\t{dish_total}")

print("----------------------------------------")

# Add tip
tip = input("Enter the Tip (optional, default is 0): ").strip()
if tip.isdigit():
    bill += int(tip)
else:
    print("Invalid tip. Proceeding without adding a tip.")

print(f"\nTotal Bill = {bill}")  # printing bill
print("Thank You for ordering!")
