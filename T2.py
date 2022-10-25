def fin(list,amount):
    list2 = []
    list3 = []
    list5 = []
    for i in range(0,amount,1):
        if list[i]%2==0:
            list2.append(list[i])
        if list[i]%3==0:
            list3.append(list[i])
        if list[i]%5==0:
            list5.append(list[i])
    return "Divides by two",list2,"Divides by three",list3,"Divides by five",list5

print("Enter the amount of elements:")
amount= int(input())
list = []
for i in range(0,amount,1):
    print("Enter ", i ," element:")
    list.append(int(input()))
print(fin(list,amount))
