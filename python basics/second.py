num=input("Enter a number\n")
num=int(num)
fact=1

def factorial(num,fact):
    while(num>=1):
        fact=fact*num
        num-=1

    print(f"Factorial of the number(non-recursive) is : {fact}")

def rec_factorial(num):
    if(num>=1):
        return num*rec_factorial(num-1)
    else:
        return 1
    


factorial(num,fact)
k=rec_factorial(num)
print(f"factorial of the number (recursive ) : {k}")
