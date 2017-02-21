#判断输入的日期是今年的第几天?
date=input("请输入日期:(20170214): ");
year=int(date[:4])
month=int(date[4:6])
day=int(date[-2:len(date)])

month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
data = sum(month_day[:month-1],day)
print(data)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if month > 2:
        data = data + 1
print("是第 %d 天" % (data))