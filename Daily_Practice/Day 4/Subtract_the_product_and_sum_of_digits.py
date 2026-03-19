Num = int(input("Enter a number: "))
Product = 1
Sum = 0 
while Num > 0:
    digit = Num % 10
    Product *= digit
    Sum += digit
    Num //= 10  
Result = Product - Sum
print("The result is:", Result)