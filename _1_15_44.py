array=[]
for i in range(1,10001):
    array.append(i*(3*i-1)/2)

for m in range(0,9999):
    for n in range(m+1,10000):
        t=array[m]+array[n]
        if (t in array)and(array[n]-array[m] in array):
            d=array[n]-array[m]
            print(d)


