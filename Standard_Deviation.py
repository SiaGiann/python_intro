import math
import random as rn

N = int(input('Please enter the number of random integers: '))
L = [rn.randint(1,20) for i in range(N)]

def stats(L):
    M = sum(L) / len(L)
    diff = [(x - M) ** 2 for x in L]
    return M, math.sqrt(sum(diff)/(len(L)-1))

print('List: ', L)
M, sd = stats(L)
print('Average: ', M, ', Standard deviation: ', sd)
