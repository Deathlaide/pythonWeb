def func(number):
    temp = number
    reversed = 0
    while (temp!=0):
        reversed = (reversed *10) + (temp % 10)
        temp=temp//10
    if(number==reversed):
        return True
    else:
        return False
x = int(input("Enter a number: "))
if(func(x)==True):
    print("Palindrome")
else:
    print("Not a palindrome")

