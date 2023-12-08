# While
count = 0
number_sum = 0

number = int(input("Enter a number: "))

while number != -1:
    count += 1
    number_sum += number
    number = int(input("Enter a number: "))

average_num = number_sum / count

print(average_num)

