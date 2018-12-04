from functools import reduce

def add_all (a,b):
    return a+b

nums=[]
n=int(input("How many numbers you want to input? "))
print("Enter {} numbers:".format(n))
for i in range(n):
    a=int(input())
    nums.append(a)

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda a,b:a+b,doubles)

print(evens)

print(doubles)

print(sum)