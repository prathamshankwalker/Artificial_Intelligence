num=input("Enter a number\n")
num=int(num)

largest=0
smallest=9
second_largest=0
second_smallest=9
def sum_second_largest_smallest(num,largest,smallest,second_largest,second_smallest):
    while(num!=0):
        dig=num%10
        if(largest<dig):
            second_largest=largest
            largest=dig
        elif(dig>=second_largest):
            second_largest=dig
          
        if(smallest>dig):
            second_smallest=smallest
            smallest=dig
        elif(second_smallest>=dig):
            second_smallest=dig

        num=int(num/10)

    sum=second_smallest+second_largest
    print(f"The second largest number is {second_largest} and second smallest number is {second_smallest} and their sum is : {sum}")

sum_second_largest_smallest(num,largest,smallest,second_largest,second_smallest)