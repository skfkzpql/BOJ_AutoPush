s = open(0).read()

if len(s) > 0:

    l=['(']
    tmp = ''
    for i in range(len(s)):
        if s[i] == '-':
            l.append(str(int(tmp)))
            tmp = ''
            l.append(')-(')
        elif s[i] == '+':
            l.append(str(int(tmp)))
            tmp = ''
            l.append(s[i])
        else:
            tmp += s[i]
            if i == len(s) - 1:
                l.append(str(int(tmp)))
                l.append(')')
    print(eval(''.join(l)))

else:
    print(0)
