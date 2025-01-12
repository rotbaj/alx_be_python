def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    title = "Shopping List Manager"
    print(f"\n{title}")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ").strip()  # Get user input

        if choice == '1':  # Add an item
            item = input("Enter the item to add: ").strip()
            if item:  # Check if the input is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Invalid input. Please enter a valid item name.")

        elif choice == '2':  # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")

        elif choice == '3':  # View the list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break

        else:  # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()