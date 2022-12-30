
number = int(input("Say gir kardeş : "))

number_of_zero = 0

while number >= 10:
    if number % 10 == 0:
        number_of_zero += 1
        number = number // 10

    else:

        number = number // 10

print(f"{number_of_zero} tane 0 var")
