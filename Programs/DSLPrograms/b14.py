l=[]
n=int(input("Enter number of marks in array:"))
for i in range(0,n):
    x=float(input("Enter percentage:"))
    l.append(x)
print("Array",l)

def selection_sort():
    for i in range(0,n):
        for j in range(i,n):
            if l[i]>l[j]:
                c=l[i]
                l[i]=l[j]
                l[j]=c
                
            else:
                l[i]=l[i]
                l[j]=l[j]

selection_sort()
print("Selection sort - Top five",l[n-5:n])

def bubble_sort():
    
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            c=l[i]
            l[i]=l[i+1]
            l[i+1]=c
            
        else:
            l[i]=l[i]
            l[i+1]=l[i+1]
                
      
bubble_sort()
print("Bubble sort - Top five",l[n-5:n])
