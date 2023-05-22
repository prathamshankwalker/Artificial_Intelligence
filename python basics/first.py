num=input("Enter a number\n")
num=int(num)
i=2
def is_odd_even(num):
    if(num%2==0):
        print("number is even")
    else:
        print("number is odd")

def is_prime(num,i):
    if (num==1):
        print("not prime")
    else:
        while (i<=num):
            if(num%i==0 and i<num):
                print("not prime")
                i+=1
                exit()
            elif(num%i==0 and i==num):
                print("number is prime")
                is_odd_even(num)
                i+=1
            else:
                i+=1
        
is_prime(num,i)