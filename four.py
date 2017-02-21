#输入3个数，按大小排序
list=[]
for i in range(3):
    x=int(input("输入:\n"));
    list.append(x);
list.sort();

for i in range(3):
    print(list[i]);
