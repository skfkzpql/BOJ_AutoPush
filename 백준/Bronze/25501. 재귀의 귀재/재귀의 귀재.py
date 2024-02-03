def isPalindrome(s,i):
    if len(s) == 0:
            return 1, i + 1
    if len(s) == 1:
            return 1, i + 1
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1],i+1)
    else:
        return 0, i+1

l = list(map(str,open(0).read().rsplit()))[1:]

for j in l:
    print(*isPalindrome(j,0))