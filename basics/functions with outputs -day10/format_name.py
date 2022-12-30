def format_name(name,last_name):
    formated =""
    formated += str(name[0]).upper()
    for n in range(1,len(name)):
        formated+=name[n]
    formated+=" "
    formated += str(last_name[0]).upper()
    for n in range(1,len(last_name)):
        formated+=last_name[n]
    print(formated)

f_name = input("Name: ").lower()
#l_name = input("Last Name: ").lower()

format_name(f_name,"töre")