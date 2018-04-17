import sys

# read input and strip number of test cases
input_array = sys.stdin.read().splitlines()
input_array.remove(input_array[0])

# function to print even-indexed and odd-indexed characters as 2 space-separated strings
def even_odd_print(str):
    even_char = []
    odd_char = [] 
    for index, char in enumerate(str):
        if index == 0 or index % 2 ==0:
            even_char.append(char)
        else:
            odd_char.append(char)
    return "".join(even_char) + " " + "".join(odd_char)

for i in input_array:
    print(even_odd_print(i))