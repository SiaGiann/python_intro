def myrange(N, ratio):
    for a in range(N):
        if a==0:
            x = 1
        else:
            x = x * ratio
        yield x

for i in myrange(5, 10):
    print(i)

print()

for i in myrange(6,2):
    print(i)
