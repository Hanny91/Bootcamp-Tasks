# Calculates and prints the total thriatlon time
swimming_time = int(input("Swimming time in whole minutes: "))
cycling_time = int(input("Cycling time in whole minutes: "))
running_time = int(input("Running time in whole minutes: "))

total_time = swimming_time + cycling_time + running_time
print(f"Your thriathlon time is {total_time} minutes.")

# Prints the relevant award given a participants total thriatlon time
if total_time <= 100:
    print("You've been awarded Provincial Colours")
elif total_time <= 105:
    print("You've been awarded Provincial Half colours")
elif total_time <= 110:
    print("You've been awarded a Provincial Scroll")
else:
    print("Sorry, you don't qualify for an award.")
