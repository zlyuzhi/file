



for a in range(10):
    for b in range(20,30):
        global c
        c =a+b
        yield c
print(c)