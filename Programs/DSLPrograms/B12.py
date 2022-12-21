#binary search

l=[]
x=int(input("Enter number of friends in phonebook:"))
for i in range(x):
    n=input("Enter Name and number of friend:")
    l.append(n.split())
print("Sorted Phonebook",sorted(l))

q=[]
for j in l:
    q.append(j[0])
p=sorted(q)

y=input("Enter name of friend to find:")


def binary_search():
    k=p.index(y)
    le=len(p)
    low=0
    high=le-1
    s=low+high
    mid=s//2

    if p[mid]<p[k]:
        low=mid+1
        high=high
        mid=(low+high)//2
        
    elif p[mid]>p[k]:
        low=low
        high=mid-1
        mid=(low+high)//2
        
    elif p[mid]==p[k]:
         print("The friend", p[k], "is present at", k+1,"position")
       
        
    
if y in p:
    binary_search
    k=p.index(y)
    print("The friend", p[k], "is present at", k+1,"position")


else:
    print("Friend not present \n Please insert")
    m=input("Enter Name and number of friend:")
    l.append(m.split())
    print("Sorted Phonebook",sorted(l))



