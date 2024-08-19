v6 = [
    53, 57, 46, 57, 40, 57, 43, 96, 24, 93, 
    85, 21, 87, 89, 68, 43, 22, 81, 24, 68, 
    43, 87, 21, 82, 68, 85, 72, 25, 85, 9, 98
]
v7 = 31  # Expected length of the string

correct_string = ''.join(chr(x + 27) for x in v6)
print(f"The correct string is: {correct_string}")
