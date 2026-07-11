import json

food_inventory = []
def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(food_inventory, file, indent=4)

def load_inventory():
    global food_inventory
    try:
        with open("inventory.json", "r") as file:
            food_inventory = json.load(file)
    except FileNotFoundError:
        pass  # If the file doesn't exist, we start with an empty inventory

def view_inventory():
    if not food_inventory:
            print("Inventory is empty.")
    else:
            print("\nCurrent Inventory:")
            for item in food_inventory:
                 print(f"- {item['amount']} - {item['name']} - (Best before: {item['best_before']})")

def edit_food():
    view_inventory()


def search_inventory():
    if not food_inventory:
        print("Inventory is empty.")
    else:
        search_name = input("Enter the food name to search for: ")
        found_items = [item for item in food_inventory if search_name.lower() == item['name'].lower()]
        if found_items:
            print(f"Found {len(found_items)} item(s):")
            for index, item in enumerate(found_items, start=1):
                print(f"{index}. {item['amount']} - {item['name']} - (Best before: {item['best_before']})")
        else:
            print("No matching items found.")

    

load_inventory()

while True:
    print("\nFood Inventory Tracker")
    print("1. Add Food")
    print("2. View Inventory")
    print("3. Remove Food")
    print("4. Search Food")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        # Add Food
        food_name = input("Enter food name: ")
        amount = int(input("How many: ")) 
        best_before = input("Enter best before date (YYYY-MM-DD): ")
        # location = input("Enter location: ")

        food = {
          "name": food_name,
          "amount": amount,
          "best_before": best_before,
        #  "location": location
      }
                
        food_inventory.append(food)

        print(f"{amount} {food_name}(s) added to inventory.")

        save_inventory()


    elif choice == "2":
        # View Inventory
        view_inventory()

    elif choice == "3":        
        # Remove Food
        if not food_inventory:
            print("Inventory is empty.")
        else:
            for index, item in enumerate(food_inventory):
                print(f"{index + 1} {item['name']} ")

            item_number = int(input("Enter the number of the food item to remove: "))

            if item_number < 1 or item_number > len(food_inventory):
                print("Invalid item number.")                
            else:
                removed_item = food_inventory.pop(item_number - 1)
                print(f"{removed_item['name']} removed from inventory.")

                save_inventory()

    elif choice == "4":
        # Search Food
        if not food_inventory:
            print("Inventory is empty.")
        else:
            search_name = input("Enter the food name to search for: ")
            found_items = [item for item in food_inventory if search_name.lower() == item['name'].lower()]
            if found_items:
                print(f"Found {len(found_items)} item(s):")
                for index, item in enumerate(found_items, start=1):
                    print(f"{index}. {item['amount']} - {item['name']} - (Best before: {item['best_before']})")
            else:
                print("No matching items found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice")











