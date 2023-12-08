#Asks for the user to input a sentence and prints it's lenght

str_manip = input("Enter a sentence: ")
print(len(str_manip))

#Replaces every occurence of the last letter for @
last_letter = str_manip[-1]
replaced = str_manip.replace(last_letter, "@")
print(replaced)

#Prints the last 3 letters in reverse
last_three = str_manip[-3:]
print(last_three[::-1])