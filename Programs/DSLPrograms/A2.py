def read(a,m):
    print("enter array elements")
    for i in range(m):
        num=int(input("enter number"))
        a.append(num)
    

def dis(a,m):
    print("entered array elements are as follows:")
    for i in range(m):
        print(a[i])

def ave_marks(a,m):
    sum=0
    count=0
    for i in range(m):
        if(a[i]>=0):
            sum=sum+a[i]
            count=count+1   # total present students
    avg=sum/count
    print("Average marks is {}".format(avg))
    print("Total no. of absent students {}".format(m-count))
    
def min_max(a,m):
    min1=-1
    max1=101
    for i in range(m):
        if(a[i]>=0):
            if(a[i]>min1):
                hs=a[i]
                min1=a[i]
            if(a[i]<max1):
                ls=a[i]
                max1=a[i]
    print("Highest number is {}".format(hs))
    print("Lowest number is {}".format(ls))
        

def max_count(a,m):
    temp=[]
    for i in range(101):
        temp.append(0)
    for i in range(m):
        if(a[i]>=0):
            temp[a[i]]=temp[a[i]]+1
    print(temp)
    min1=-1
    for i in range(101):
           if(temp[i]>min1):
                max_c=temp[i]
                min1=temp[i]
                ans=i
    print("The Highest count is {}".format(ans))
    
def main():
    a=[]
    m=int(input("enter m"))
    
    read(a,m)
    dis(a,m)
    ave_marks(a,m)

    min_max(a,m)
    max_count(a,m)
    
if __name__ == "__main__":
    main()
