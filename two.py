#一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
import math
for i in range(10000):
    a=int(math.sqrt(i+100));
    b= int(math.sqrt(i + 268));
    if(a*a==i+100)and(b*b==i+268):
        print(i);


