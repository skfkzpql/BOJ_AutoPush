import math
def solution(numer1, denom1, numer2, denom2):
    a=numer1*denom2
    b=numer2*denom1
    c=a+b
    d=denom1*denom2
    e=math.gcd(c,d)
    answer=[c/e,d/e]
    return answer