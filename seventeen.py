#写入字符到本地.txt 文件
fw=open("seventeen.txt",'w');
ss=input("输入字符:\n");
fw.write(ss);
fw.close();

fw=open("seventeen.txt",'r');
ns=fw.read();
fw.close();
print(ns)

