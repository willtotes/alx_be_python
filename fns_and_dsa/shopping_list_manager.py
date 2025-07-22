

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Add item: ")
            shopping_list.append(item)
            print(f"{item}, added to the list")
            pass
        elif choice == "2":
            item = input("Remove Item: ")
            shopping_list.remove(item)
            print(f"{item}, has been removed!")
            pass
        elif choice == "3":
            item = input("View List: ")
            print(f"Current List: {shopping_list}")
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

# Not done still need fixes