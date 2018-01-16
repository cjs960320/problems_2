#dic1={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'\"':0}

f=open('words.txt')
list1=f.read()
list2=list1.split(',')

dic1={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,'\"':0}
n=0
array=[]
for i in range(1,100000):
    array.append(i*(i+1)/2)

for j in list2:
    print(j)
    sum=0
    for k in j:
        sum=sum+dic1[k]
    print(sum)
    if sum in array:
        n=n+1

print(n)