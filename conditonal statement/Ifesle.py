name = input("enter  your name: ")
age = int(input("enter your  age: "))
citizenship = input("do you have Nepali citizen ship(y/n)").lower()
if 18>=age>=16 and citizenship == 'y':
    print("You are eligible for NEB examination")
else:
    print("You cannot Give NEB Examination")
print("Good Luck")
