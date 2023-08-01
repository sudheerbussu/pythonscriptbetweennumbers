# Reading user data

print('enter any number between 1 -100.....\n')
number = int(input())

# printing user entered value
print(f'you are entered {number}')


if 0 <= number <= 25:  # validation 1
    print("Number is between 0 and 25.")

elif 26 <= number <= 50:  # validation 2
    print("Number is between 26 and 50.")

elif 51 <= number <= 75:  # validation 3
    print("Number is between 51 and 75.")

elif 76 <= number <= 100:  # validation 4
    print("Number is between 76 and 100.")
else:    # fails
    print("Number is out of range (not between 0 and 100).")


