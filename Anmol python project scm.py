import math
x=[10,7,9,11,15,12,13,11,9,10]

def m(o):
    sum=0
    for i in o:
        sum=sum+i
    mean = sum/len(o)
    return mean

a=m(x)

def sd(p,a):
    sum1=0
    for i in p:
        b=i-a
        sum1=sum1+(pow(b,2))
    s=math.sqrt(sum1/len(p))
    return s




print('Mean is  ',m(x))
print('SD is  ',sd(x,a))
print('variance  ',sd(x,a)**2)
