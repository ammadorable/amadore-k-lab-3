# this function adds two numbers
def add(x, y):
    return x + y

# this function subtracts two numbers
def sub(x, y):
    return x - y

# this function multiplies two numbers
def mul(x, y):
    return x * y

# this function divides two numbers
def div(x, y):
    return x / y

x = int(input("enter your first number: "))
y = int(input("enter your second number: "))

print("add:", add(x, y))
print("subtract:", sub(x, y))
print("multiply:", mul(x, y))
print("divide:", div(x, y))

