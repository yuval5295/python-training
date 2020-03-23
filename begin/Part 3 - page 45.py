before=0
last=1
while True:
    if last < 10000:
        print(last)
        last = last + before;
        before = last - before;
    else:
        break