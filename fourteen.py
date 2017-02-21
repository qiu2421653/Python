#输入三个数字比较大小，从大到小输出
def opr(i,j):
  if(i>j):
      return i,j;
  else:
      return  j,i;



x=int(input("输入第一个数:\n"));
y=int(input("输入第二个数:\n"));
z=int(input("输入第三个数:\n"));

x,y=opr(x,y);
x,z=opr(x,z);
y,z=opr(y,z);

print(x,y,z);