import sys
while True:
    sentence = sys.stdin.readline().rstrip()
    s=1
    if sentence == '.':
        break
    l=[]
    for i in sentence:
        if i == '(' or i == '[':
            l.append(i)
        elif i == ')':
            if len(l)!=0:
                if l.pop() !='(':
                    s=0
                    break
            else:
                s=0
                break
        elif i == ']':
            if len(l)!=0:
                if l.pop() !='[':
                    s=0
                    break
            else:
                s=0
                break
    if s == 1 and len(l) == 0:
        print("yes")
    else:
        print("no")
