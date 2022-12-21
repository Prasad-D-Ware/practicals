def read(x,p):
    for i in range(p):
        num=int(input("enter number "))
        x.append(num)
        
def dis(x,p):
    for i in range(p):
        print(x[i])
    

def cric_bad_intersection(a,b,l,m):
    res=[]
    for i in range(l):
        for j in range(m):
            if(a[i]==b[j]):   # common elements in two sets
                res.append(a[i])
                break
    print(res)

def cric_bad_foot_intersection(a,b,c,l,m,n):
    res=[]
    for i in range(l):
        for j in range(m):
            for k in range(n):
                if(a[i]==b[j] and a[i]==c[k]):  # common elements in all three sets
                    res.append(a[i])
                    break
    print(res)

    

def cric_bad_union(a,b,l,m):
    res=[]
    for i in range(l):  # copy A set into resultant set
        res.append(a[i])
        
    for j in range(m):
        flag=0
        for i in range(l):
            if(b[j]==res[i]):  # check for set B elements in resultant set
                flag=1
                break
        if(flag==0):     # if not present then append into resultant set
            res.append(b[j])
            
    print(res)

    print("The number of students who play neither cricket nor badminton")
    print(len(total)-len(res))   # universal set - union of cricket and badminton 

def cric_foot_not_bad(a,b,c,l,m,n):
    res=[]
    for i in range(l):
        for j in range(n):
            if(a[i]==c[j]):   # common elements in two sets i.e. cricket and football
                res.append(a[i])
                break
    res1=[]
    for i in range(l):
        for j in range(m):
            for k in range(n):
                if(a[i]==b[j] and a[i]==c[k]):  # common elements in all three sets
                    res1.append(a[i])
                    break
    print(len(res)-len(res1))
    

total = []   # to create Universal Set which contains nos from 1 to 20
for i in range(1,21):
    total.append(i)
print("\n")
print("Universal set contains the numbers from 1 to 20")
print("\n")



def main():
    
    a=[]    # the set of students who play cricket
    b=[]    # the set of students who play badminton    
    c=[]    # the set of students who play football
    l=int(input("enter l for cricket set "))
    print("enter the set of students who play cricket")
    read(a,l)
    print("entered set for cricket is as follows ")
    dis(a,l)
    
    m=int(input("enter m for badminton set "))
    print("enter the set of students who play badminton")
    read(b,m)
    print("entered set for badminton is as follows ")
    dis(b,m)
    
    n=int(input("enter n for football set "))
    print("enter the set of students who play football")
    read(c,n)
    print("entered set for football is as follows ")
    dis(c,n)
    
    print("The students who play both cricket and badminton")
    cric_bad_intersection(a,b,l,m)

    print("The students who play cricket, badminton and football")
    cric_bad_foot_intersection(a,b,c,l,m,n)

    print("The students who play either cricket or badminton or both")
    cric_bad_union(a,b,l,m)

    print("The number of students who play cricket and  football but not badminton")
    cric_foot_not_bad(a,b,c,l,m,n)
    
if __name__ == "__main__":
    main()
