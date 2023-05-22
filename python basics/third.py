num=input("Enter a number\n")
num=int(num)
rev=0
def reverse(num,rev):
    while(num!=0):
        remainder = num % 10
        rev = rev * 10 + remainder
        num=int(num/10)
    return rev

def palindrome(num,rev):
    k=num
    if(k==reverse(num,rev)):
        print("number is a palindrome")

while(True):
    print("1. Reverse the number ")
    print("2. Check if number is palindrome ")
    k=int(input())

    if(k==1):
        r=reverse(num,rev)
        print(f"reversed number is : {r}")
        exit()
    elif(k==2):
        palindrome(num,rev)
        exit()
    else:
        print("invalid choice , enter again : ")

        

        