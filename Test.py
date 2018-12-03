#define function part

def count(ls):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

#input part

lst=[]
n=int(input("How many numbers you want to input? "))
print("Enter {} numbers:".format(n))
for i in range(n):
    a=int(input())
    lst.append(a)

#calc part

even,odd=count(lst)

print('Even: {} and Odd: {}'.format(even,odd))