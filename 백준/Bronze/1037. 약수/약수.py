import math
import sys

T, *l = map(int,sys.stdin.read().rsplit())

l.append(max(l)*min(l))
print(math.lcm(*l))
