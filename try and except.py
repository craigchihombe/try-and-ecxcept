#try and except
try:
    number = int(input("Enter the number: "))
    print("The number enterd is ",number)
    
except ValueError as ex:
    print("Exception is ",ex)