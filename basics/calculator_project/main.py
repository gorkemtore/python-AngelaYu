def calculate(n1,n2,operation_type):
    if(len(operation_type))==1:
        
        if operation_type=="-":
            return n1-n2
        elif operation_type=="+":
            return n1+n2
        elif operation_type=="/":
            return n1/n2
        elif operation_type=="*":
            return n1*n2

control_continue = True
num1 = int(input("Input the first number: "))
while control_continue:

    operation = input("Choose one of the given operations")
    num2 = int(input("Input the other number: "))
    result = calculate(num1,num2,operation)
    print(f"{num1} {operation} {num2} = {result}")
    control =input("Do u want continue this calculating?").lower()
    if control=="no":
        control_continue=False
        print("*****Bye*****")
    elif control=="yes":
        num1=result
    





