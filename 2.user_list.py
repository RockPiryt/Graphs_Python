# Initialize an empty list to store the numbers
numbers = []

print("Enter numbers to add to the list. Type 'ex' when you are finished:")

while True:
    user_input = input()
    
    if user_input.lower() == 'ex': 
        break   
    else:
        n = int(user_input)
        numbers.append(user_input)

# Print the final list of numbers
print("Here is the list of numbers you entered:")
print(numbers)

# Revert list
numbers.reverse()

# Połącz elementy wiersza w odwrotnej kolejności i wypisz
output_line = ' '.join(numbers)
print(output_line)