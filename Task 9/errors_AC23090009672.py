# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax error; extra space and missing parenthesis 
print("\n") # Syntax error; extra space, missing parenthesis and extra indent.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax error; Extra indentation in lines 9, 10 and 11 and extra = sign. Runtime eror; can't turn string with letters into int.
age = int(age_Str) 
print("I'm " + age_Str + " years old.") # Type error; use of Str variable instead of int for printing string. Added spaces to strings

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 #Syntax error; Extra indentation in lines 14 and 15. Type eror; can't add str and int on line below. Logical error; 6 months added to years_from_now.
total_years = age + years_from_now

print("The total number of years:" + str(total_years)) #Syntax error; extra space, missing parenthesis, extra semicolons on variable answer_years. Name error; changed answer_years for total_years. Type error: cast total_years to str

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Name error, changed total for total_years
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Syntax error; extra space and missing parenthesis. Type erorr; cast total_months to str

#HINT, 330 months is the correct answer