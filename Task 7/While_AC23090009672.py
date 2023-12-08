# Asks the user to input numbers until they input -1, 
# then calculates their average excluding -1.

number = int(input("Enter a number: "))

count = 0
number_sum = 0

while number != -1:
    count += 1
    number_sum += number
    number = int(input("Enter a number: "))


average_num = number_sum / count
print(average_num)

