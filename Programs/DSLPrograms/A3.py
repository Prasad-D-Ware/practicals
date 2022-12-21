import pandas as pd

u=[]
x=[]
y=[]
z=[]

n=int(input('Enter no of books: '))
for i in range(0,n):
    name=input('Enter Name of the book: ')
    cost=int(input('Enter cost: '))
    author=input('Enter name of author: ')
    code=int(input('Enter code of the book: '))
    x.append(name)
    y.append(cost)
    z.append(author)
    u.append(code)

data={'Code':u,'Name':x,'Cost':y,'Author':z}
df=pd.DataFrame(data)
print(df)
print('-'*20)

#1
df1=df.drop_duplicates(subset='Code', keep='first')
print('After deleting duplicate entries \n',df1)
print('-'*20)

#2
df2=df1.sort_values('Cost', ascending=True)
print(df2)
print('-'*20)

#3
df3=df1.loc[(df['Cost']>500)]
print(df3)
print('Count of books with cost>500=',len(df3))
print('-'*20)

#4
df4=df1.loc[(df1['Cost']<500)]
print(df4)
l=df4['Name'].tolist()
print(l)


