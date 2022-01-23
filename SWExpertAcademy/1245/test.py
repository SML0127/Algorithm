def myrange(start, end, step):
    r = start
    while(r<end):
        yield r
        r += step

for i in myrange(0,1,0.1):
    print(i)