num=100
list=[]
k=0
for i in range(1,num+1):
    if num%i==0:
        k=0
        for j in range(1,i+1):
          #if i%2==0:
              #break
          if i %j==0:
              k+=1
        if k==2:
            list.append(i)
           
print(max(list))