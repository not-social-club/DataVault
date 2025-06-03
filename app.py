import json
import os


# ========== Load Data ==========
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)


data = load_data()
categories = data['categories']
cities = data['cities']


# ========== Inventory ==========
inventory_file = 'inventory.json'


def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as file:
            return json.load(file)
    return []


def save_inventory():
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)


inventory = load_inventory()


# ========== UI ==========
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
[ SYSTEM ] :: DataVault Initialized
[ STATUS ] :: Your data fully under control.
[  NODE  ] :: Not Social Club | DataVault v1.0
''')


def menu():
    print('''
[1] New Inventory
[2] View Inventory
[3] Edit Inventory
[4] Import Inventory (JSON)
[5] Export Inventory (JSON)
[0] Exit
''')


# ========== Functions ==========

def new_inventory():
    while True:
        print('\nSelect Category:')
        for idx, category in enumerate(categories.keys(), 1):
            print(f"[{idx}] {category}")
        print("[0] Return")

        try:
            cat_choice = int(input("\nInput option number: ").strip())

            if cat_choice == 0:
                break

            category_list = list(categories.keys())

            if 1 <= cat_choice <= len(category_list):
                selected_category = category_list[cat_choice - 1]
                items = categories[selected_category]

                print(f"\nSelected Category: {selected_category}")
                for idx, item in enumerate(items, 1):
                    print(f"[{idx}] {item}")
                print("[0] Return")

                item_choice = int(input("\nSelect item number: ").strip())

                if item_choice == 0:
                    continue

                if 1 <= item_choice <= len(items):
                    selected_item = items[item_choice - 1]

                    # quantity
                    quantity = int(input("Enter quantity: ").strip())

                    # location
                    print("\nSelect Location:")
                    for idx, city in enumerate(cities, 1):
                        print(f"[{idx}] {city}")
                    city_choice = int(input("\nSelect location number: ").strip())

                    if 1 <= city_choice <= len(cities):
                        selected_city = cities[city_choice - 1]

                        # add to inventory
                        inventory.append({
                            "Category": selected_category,
                            "Item": selected_item,
                            "Quantity": quantity,
                            "Location": selected_city
                        })

                        save_inventory()

                        print("\nItem added to inventory!\n")

                    else:
                        print("Invalid location.")

                else:
                    print("Invalid item selection.")

            else:
                print("Invalid category.")

        except ValueError:
            print("Invalid input. Enter a number.")


def view_inventory():
    if not inventory:
        print("\nInventory is empty.\n")
        return

    print("\n========= INVENTORY =========")
    for idx, entry in enumerate(inventory, 1):
        print(f"[{idx}] {entry['Item']} | Qty: {entry['Quantity']} | Location: {entry['Location']} | Category: {entry['Category']}")
    print("==============================\n")


def export_inventory():
    filename = input("Enter filename to export (without .json): ").strip()
    if not filename:
        filename = "inventory_export"

    with open(f"{filename}.json", 'w') as file:
        json.dump(inventory, file, indent=4)

    print(f"\nInventory exported to {filename}.json\n")


def import_inventory():
    filename = input("Enter filename to import (without .json): ").strip()
    if not filename:
        filename = "inventory_export"

    try:
        with open(f"{filename}.json", 'r') as file:
            imported_data = json.load(file)
            if isinstance(imported_data, list):
                inventory.extend(imported_data)
                save_inventory()
                print(f"\nInventory imported from {filename}.json\n")
            else:
                print("Invalid JSON format.")

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error reading JSON file.")


def edit_inventory():
    view_inventory()

    if not inventory:
        return

    try:
        idx = int(input("Select item number to edit (0 to cancel): ").strip())

        if idx == 0:
            return

        if 1 <= idx <= len(inventory):
            entry = inventory[idx - 1]

            print(f"\nEditing: {entry['Item']} | Qty: {entry['Quantity']} | Location: {entry['Location']}")

            print('''
[1] Change Quantity
[2] Change Location
[3] Remove Item
[0] Cancel
''')
            choice = int(input("Select option: ").strip())

            if choice == 1:
                new_qty = int(input("Enter new quantity: ").strip())
                entry['Quantity'] = new_qty
                save_inventory()
                print("Quantity updated.")

            elif choice == 2:
                print("\nSelect new location:")
                for idx_city, city in enumerate(cities, 1):
                    print(f"[{idx_city}] {city}")
                city_choice = int(input("\nSelect location number: ").strip())

                if 1 <= city_choice <= len(cities):
                    entry['Location'] = cities[city_choice - 1]
                    save_inventory()
                    print("Location updated.")
                else:
                    print("Invalid location.")

            elif choice == 3:
                inventory.pop(idx - 1)
                save_inventory()
                print("Item removed.")

            elif choice == 0:
                return
            else:
                print("Invalid option.")

        else:
            print("Invalid item number.")

    except ValueError:
        print("Invalid input.")


# ========== Main Loop ==========

def main():
    banner()

    while True:
        menu()

        try:
            choice = int(input("\nInput option number: ").strip())

            if choice == 1:
                new_inventory()
            elif choice == 2:
                view_inventory()
            elif choice == 3:
                edit_inventory()
            elif choice == 4:
                import_inventory()
            elif choice == 5:
                export_inventory()
            elif choice == 0:
                print("\nExiting...\n")
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Invalid input. Enter a number.")


if __name__ == "__main__":
    main()

# made by @fbreseghello | github.com/fbreseghello