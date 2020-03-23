NUM=100
i=0
for i in xrange(NUM):
    if i%7 == 0 and i != 0:
        print(i)
    elif i%10==7 or i//10==7:
        print(i)
    else:
        continue