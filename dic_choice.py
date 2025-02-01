def get_user_dict():
    user_dict = {}
    n = int(input("Enter the number of key-value pairs: "))
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        user_dict[key] = value
    return user_dict


def display_menu():
    print("\nChoose a dictionary function to apply:")
    print("1. Get keys")
    print("2. Get values")
    print("3. Get items (key-value pairs)")
    print("4. Get value for a specific key")
    print("5. Remove a key-value pair")
    print("6. Check if a key exists")
    print("7. Clear dictionary")
    print("8. Exit")


def main():
    user_dict = get_user_dict()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Keys:", list(user_dict.keys()))
        elif choice == "2":
            print("Values:", list(user_dict.values()))
        elif choice == "3":
            print("Items:", list(user_dict.items()))
        elif choice == "4":
            key = input("Enter the key to get its value: ")
            print("Value:", user_dict.get(key, "Key not found"))
        elif choice == "5":
            key = input("Enter the key to remove: ")
            removed_value = user_dict.pop(key, "Key not found")
            print("Removed value:", removed_value)
        elif choice == "6":
            key = input("Enter key to check: ")
            print("Exists:" if key in user_dict else "Does not exist")
        elif choice == "7":
            user_dict.clear()
            print("Dictionary cleared!")
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
