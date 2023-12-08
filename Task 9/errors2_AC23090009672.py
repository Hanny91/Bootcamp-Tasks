# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion"     # Syntax error; missing parenthesis. Removed capital L for printed string syntax.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #Runtime error; missing f. Runtime error; swapped variables

print(full_spec)    # Syntax error; missing parenthesis and extra space.