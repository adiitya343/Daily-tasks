import string  # importing string to access string

# defining fucion for to excute function when choice made
def apply_string_function():
    functions = {
        '1': 'upper',
        '2': 'lower',
        '3': 'capitalize',
        '4': 'title',
        '5': 'swapcase',
        '6': 'strip',
        '7': 'replace',
        '8': 'find',
        '9': 'count'
    }
    
    print("Choose a string function:")
    for key, value in functions.items():
        print(f"{key}. {value}")
    
    # choice made by user
    choice = input("Enter the number corresponding to the function: ")
    
    if choice not in functions:
        print("Invalid choice! Please select a valid option.")
        return
    
    # user input string/sentence however he wants 
    user_string = input("Enter a string: ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        result = getattr(user_string, functions[choice])()
    elif choice == '7':  # replace
        old = input("Enter the substring to replace: ")
        new = input("Enter the new substring: ")
        result = user_string.replace(old, new)
    elif choice == '8':  # find
        sub = input("Enter the substring to find: ")
        result = user_string.find(sub)
    elif choice == '9':  # count
        sub = input("Enter the substring to count: ")
        result = user_string.count(sub)
    
    print(f"Result: {result}")  # print result

apply_string_function()
