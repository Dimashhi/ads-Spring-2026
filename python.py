#1 ------------------------------
# n = int(input())
# sum = 0
# i =0
# for digit in str(n):
#     i+=1
#     if int(digit) % 2 == 0:
#         sum+=1
# if sum==i:
#     print("Valid")
# else:
#     print("Not valid")
#2 ------------------------------
# L, W = map(int, input().split())
# print(L * W)
#3
# L, W = map(int, input().split())
# if L > W:
#     print(L - W)
# elif L<W:
#     print("Insufficient Funds")
# else:
#     print(0)
#4
# import math
# n = int(input())
# pi = 3.14159
# t = pi * n * n
# print(f"{t:.2f}")
#5
# list_ = list(map(int, input().split()))
# print("Result:",list_[0]+list_[2], list_[1]+list_[3])
#6
# Input example: abcde 10
#6
# l, w = input().split()
# L = str(l)
# W = float(w)
# print("Student:",L+',',"GPA:",W)
#7
s1,s2,i1,i2 = input().split()
I1 = int(i1)
I2 = int(i2)
x1 = I1 * (1+I2/100)
x2 = I1 + (I2 * 500)
if s1 == "Manager":
 print("Name:",s2+',',"Total:", f"{x1:.2f}")
elif s1 == "Developer":
    print("Name:",s2+',',"Total:",f"{x2:.2f}")
else:
    print(I1)
    


    