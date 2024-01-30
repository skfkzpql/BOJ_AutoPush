a=int(input())
l=[]
num=666
count=0

while True:
    if '666' in str(num):
        count+=1
    if count == a:
        print(num)
        break
    num+=1