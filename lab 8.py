# Q.1: Sum all items in a list
# Take input from the user 
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# initialize sum variable
sum_of_numbers = 0

# Loop through the list 
for num in numbers:
    sum_of_numbers += num

# Print the result
print("Sum of all items in the list:", sum_of_numbers)

#################################################################################################################

# Q.2: Find the largest and smallest number without builtin functions

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Initialize variables with first element of the list
smallest = numbers[0]
largest = numbers[0]

# Loop through the list to find smallest and largest numbers
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

# Print the results
print("Smallest number in the list:", smallest)
print("Largest number in the list:", largest)

#################################################################################################################

# Q.3: Find duplicate values in a list and display those

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Initialize an empty dictionary to keep track of occurrences
occurrences = {}
duplicates = []

# Count occurrences of each element
for num in numbers:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

# Identify duplicates (numbers appearing more than once)
for num, count in occurrences.items():
    if count > 1:
        duplicates.append(num)

# Print duplicates if any, else print no duplicates found
if duplicates:
    print("Duplicate values found:", duplicates)
else:
    print("No duplicate values found.")

#################################################################################################################

# Q.4: Split a list into two parts

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# Take user input for split index
split_index = int(input("Enter the index to split the list: "))

# Split the list manually
first_part = numbers[:split_index]
second_part = numbers[split_index:]

# Print both parts
print("First part of the list:", first_part)
print("Second part of the list:", second_part)

#################################################################################################################

# Q.5: Traverse the list in reverse order and print elements with original index

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("List in reverse order with original indexes:")
for i in range(len(numbers) - 1, -1, -1):
    print(f"Index {i}: {numbers[i]}")
