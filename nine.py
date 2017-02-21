#计算输入的数字和字母个数
dig=0;
str=0;
x=input("输入参数:\n");
for i in x:
  if(i.isdigit()):
      dig=dig+1;
  elif(i.isalpha()):
      str=str+1;
print("数字 %d 个 ，字母 %d 个" %(dig,str));
