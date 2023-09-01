def square_number(num):
    return num ** 2
sample_list = [4, 5, 2, 9]
result_list = list(map(square_number, sample_list))
print("Square the elements of the list:")
print(result_list)
