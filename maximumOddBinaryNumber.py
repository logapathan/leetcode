def maximumOddBinaryNumber(s):
    l = len(s)
    a=[]
    for i in range(0,l):
        a.append(s[i])


    frequency = 0
    for i in range(0, l):

        if a[i]=="1":
            frequency=frequency+1

    cond = False
    if a[l - 1] == "1":
        cond == True
    if cond == False and frequency == 1:
        for i in range(0, l):
            if a[i] == "1":
                temp = a[i]
                a[i] = a[l - 1]
                a[l - 1] = temp
                print(a)
                break
    elif cond == False and frequency != 1:
        for i in range(0, l):
            if a[i] == "1":
                temp = a[i]
                a[i] = a[l - 1]
                a[l - 1] = temp
                break
        for i in range(1, l - 1):
            for j in range(0, l - 1):
                if a[i] == "1" and a[j] != "1":
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    break
    elif cond == True and frequency != 1:
        for i in range(1, l - 1):
            for j in range(0, l - 1):
                if a[i] == "1" and a[j] != "1":
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    break
    return a
a=input()
y=maximumOddBinaryNumber(a)
l=len(a)

z=""
for i in range(0,l):
    z=z+""+y[i]

print(z)