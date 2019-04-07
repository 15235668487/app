#空心正方形
# i=1
# while i<=4:
#     a=1
#     while a<=4:
#         if i==2 and (a==2 or a==3) or i==3 and (a==2 or a==3) :
#             print(" \t",end="")
#         else:
#             print("*\t",end="")
#         a+=1
#     print()
#     i+=1
#
#
# #菱形while
# i=1
# while i<=4:
#     a = 3
#     while a>=i:
#         print(" ", end="")
#         a -= 1
#     j=1
#     while j<=2*i-1:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1
# b=1
# while b<=3:
#     c=1
#     while c<=b:
#         print(" ",end="")
#         c+=1
#     e=5
#     while e>=2*b-1:
#         print("*",end="")
#         e-=1
#     print()
#     b+=1
#菱形for
# for i in range(1,5):
#     for j in range(i,4):
#         print(" ", end="")
#     for a in range(1,2*i):
#         print("*",end="")
#     print()
# for b in range(1,4):
#     for c in range(1,b+1):
#         print(" ",end="")
#     for d in range(2*b-1,6):
#         print("*",end="")
#     print()
#
# #9*9乘法表while
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         a=i*j
#         print(i,"*",j,"=",a,"\t",end="")
#         j+=1
#     print()
#     i+=1
# 9*9乘法表for
# for i in range(1,10):
#     for j in range(1,i+1):
#         a=i*j
#         print(i,"*",j,"=",a,"\t",end="")
#     print()
#检索两个字符相同的字符
# for a in "asdff2":
#     for b in "sfs2ad":
#         if a==b:
#             print(a)
#输出成绩
# sum=0
# i=1
# while i<=5:
#     score=int(input("请输入成绩"))
#     if score>=0:
#         sum += score
#     elif score>100 or score<0:
#         print("输入有误，退出系统")
#         break
#     i += 1
#     if i==6:
#         print("平均成绩是", sum/5)
#输入成绩if
# sum=0
# for i in range(1,6):
#     score=int(input("输入成绩"))
#     if score>=85:
#         sum=sum+1
# print("大于等于85分学生数量百分比为",sum/5*100,"%")
#输入成绩continue
# sum=0
# for i in range(1,6):
#     score=int(input("输入成绩"))
#     if score>=85:
#         sum=sum+1
#         continue
# print("大于等于85分学生数量百分比为",sum/5*100,"%")
#

#100 以内的质数
# i=2
# for i in range(2,101):
#     j=2
#     for j in range(2,i):
#         if i%j==0:
#             break
#     if j==i-1:
#           print(i)
#银行插卡
# print("请插入银行卡\n银行卡读取完成\n")
# i=1
# while i<4:
#     a=input("请输入密码：")
#     if a=="123456":
#         print("欢迎登录工商银行")
#         break
#     else:
#         print("密码错误,还剩",3-i,"次机会")
#         i+=1
#         if i==4:
#             print("银行卡已被锁，请到柜台解锁")
#         continue
#猜高低
# import random
# print("欢迎参加节目，物品已经准备好了")
# b=random.randint(1,100)
# for i in range(1,6):
#     a=  int(input("请输入价格："))
#     if a==b and i==1:
#         print("猜对了，奖励电冰箱一台")
#     elif a==b and i==2:
#         print("猜对了，奖励电视一台")
#     elif a == b and i == 3:
#         print("猜对了，奖励洗衣机一台")
#     elif a==b and i==4:
#         print("猜对了，奖励马桶盖一个")
#     elif a == b and i == 5:
#         print("猜对了，奖励洗衣粉一袋")
#     elif a>b:
#         print("高了")
#     elif a<b:
#         print("低了")








