def func(number, degree):
    a=1
    b=(1/degree)*((degree-1)*a+(number/(a**(degree-1))))
    while(abs(b-a)>0.1):
        a=b
        b=(1/degree)*((degree-1)*a+(number/(a**(degree-1))))
    return b
number = int(input("Enter a number: "))
degree = int(input("Enter the degree of a number: "))
print(func(number,degree))

