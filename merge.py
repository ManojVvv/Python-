try:
    a=int(input("Enter number of elemants in first list:"))
    b=[ ]
    for i in range(0,a):
        c=int(input("Enter elemant"))
        b.append(c)
    d=int(input("Enter number of elements in second list:"))
    e=[ ]
    for i in range(0,d):
        f=int(input("Enter element"))
        e.append(f)
    g=[ ]
    g=b+e
    g.sort()
    print("LIST1..",b)
    print("LIST2..",e)
    print("Mergad and sorted list..",g)
except valueError:
    print()
