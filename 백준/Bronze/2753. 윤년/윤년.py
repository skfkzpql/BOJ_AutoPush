a=int(input())
print('01'[(a%4==0)^(a%100==0)^(a%400==0)])