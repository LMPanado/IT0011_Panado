class Item:
    def __init__(store, item_id, name, description, price):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name.strip():
            raise ValueError("The NAME cannot be empty.")
        if not isinstance(description, str):
            raise ValueError("The DESCRIPTION must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("The PRICE must be a non-negative number.")
        
        store.item_id = item_id
        store.name = name.strip()
        store.description = description.strip()
        store.price = round(price, 2)
    
    def __str__(store):
        return f"ID: {store.item_id}\nName: {store.name}\nDescription: {store.description}\nPrice: ₱{store.price}"

class ItemManager:
    def __init__(store):
        store.items = {}

    def create_item(store, item_id, name, description, price):
        if item_id in store.items:
            return "Item ID already exists."
        store.items[item_id] = Item(item_id, name, description, price)
        return "Item added successfully."

    def read_item(store, item_id):
        return str(store.items.get(item_id, "Item not found."))

    def update_item(store, item_id, name=None, description=None, price=None):
        item = store.items.get(item_id)
        if not item:
            return "Item not found."
        if name:
            item.name = name.strip()
        if description:
            item.description = description.strip()
        if price is not None:
            item.price = round(price, 2)
        return "Item updated successfully."

    def delete_item(store, item_id):
        return "Item deleted successfully." if store.items.pop(item_id, None) else "Item not found."

    def list_items(store):
        return "\n".join(str(item) for item in store.items.values()) or "No items available."


def main():
    manager = ItemManager()
    while True:
        print("\n====================================")
        print("       Item Management System       ")
        print("====================================")
        print("1.|  Add Item")
        print("2.|  View Item")
        print("3.|  Edit Item")
        print("4.|  Delete Item")
        print("5.|  List Items")
        print("6.|  Exit")
        print("====================================\n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                print(manager.create_item(int(input("Enter Item ID: ")), input("Enter Item Name: "), input("Enter Description: "), float(input("Enter Price: ₱"))))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            print(manager.read_item(int(input("Enter Item ID: "))))
        elif choice == "3":
            try:
                item_id = int(input("Enter the new Item ID: "))
                name = input("Enter the new Name: ") or None
                description = input("Enter the new Description: ") or None
                price_input = input("Enter the new Price: ")
                price = float(price_input) if price_input else None
                print(manager.update_item(item_id, name, description, price))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            print(manager.delete_item(int(input("Enter Item ID: "))))
        elif choice == "5":
            print("\n=== Item List ===")
            print(manager.list_items())
            print("=================")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()