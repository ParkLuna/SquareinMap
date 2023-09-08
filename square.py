try:
    input_numbers = input("Enter a list of numbers separated by spaces: ").split()
    input_numbers = list(map(float, input_numbers))
except ValueError:
    print("Invalid input. Please enter a valid list of numbers separated by spaces.")
    exit()

def square_number(num):
    return num ** 2

squared_numbers = list(map(square_number, input_numbers))

print("Original List:", input_numbers)
print("Squared List:", squared_numbers)
