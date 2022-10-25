def func(number):
    temp = abs(number)
    reversed =0
    while (temp!=0):
        reversed = (reversed *10) + (temp % 10)
        temp=temp//10
    if(number<0):
        reversed=reversed*-1
    return reversed
number = int(input("Enter a number: "))
print(func(number))

