import random
def puzyrek(a):
    i=0
    j=len(a)
    while j>0:
        while i<j-1:
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
            i+=1
        i=0
        j-=1
    return a

mySpis = [random.randint(-10,50) for i in range(20)]
print(puzyrek(mySpis))