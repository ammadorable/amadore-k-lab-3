#this function adds two numbers
def add(x,y):
    print(x+y)

add(6,7)

#this function adds two numbers
def sub(x,y):
    print(x-y)

add(6,7)

#this function adds two numbers
def mul(x,y):
    print(x*y)

add(6,7)

#this function adds two numbers
def div(x,y):
    print(x/y)

add(6,7)

add(6,7)
sub(6,7)
div(6,7)
mul(6,7)

#start of program
print("welcome to my awesome calc app")
print ("what would you like to do")
print("type(a)add(s)ubetract(m)multiply(d)ivide(q)uit")

user_choice=input(": ")
#print(user_choice)
while (True): 
    user_choice=input(": ")
    if user_choice =='a':
        x=int(input("enter the first number: "))
        y=int(input("enter the second number: "))
        add(x,y)

    elif user_choice=='s':
        x=int(input("enter the first number: "))
        y=int(input("enter the second number: "))
        sub(x,y)

    elif user_choice=='d':
        x=int(input("enter the first number: "))
        y=int(input("enter the second number: "))
        div(x,y)

    elif user_choice=='m':
        x=int(input("enter the first number: "))
        y=int(input("enter the second number: "))
        mul(x,y)

    elif user_choice=='q':
        print("closing program")
        break

    else:
        print("invalid input dummby")