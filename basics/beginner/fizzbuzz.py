for i in range (1,101):
    if i%15 == 0:
        print("Fizzbuz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%3==0 and i%5!=0:
        print("Fizz")
    else:
        print(i)