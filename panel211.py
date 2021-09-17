def bubblesort (array, marray, barray):
    n = len(array)

    for i in range (n-1):
        for j in range (0, n-i-1):
            if array[j] < array[j + 1] :
                array[j], array[j+1] = array[j + 1], array[j]
                marray[j], marray[j+1] = marray[j + 1], marray[j]
                barray[j], barray[j+1] = barray[j + 1], barray[j]


def TYPOS_EMB(ag, ar):
    if  int (ag )>= 40 and int (ag) <= 50:
        print("vaxin tipe 1 amka ", (ar))

    if  int (ag) >= 51 and int (ag) <= 60:
        print("vaxin tipe 2 amka ", (ar))

    if  int (ag) >= 61 and int (ag) <= 70:
        print("vaxin tipe 3 amka ", (ar))

    if int (ag) >= 71:
        print("vaxin tipe 4 amka ", (ar))


ilikia = []
arimo = []
gen = []

gcount = 0
count = 0
x = 0

while x < 1:
    count +=1
    i = 0
    amka = input("give amka ")
    arimo.append(amka)
    age = input("give age ")
    if int(age) <= 39:
        x = 1
        i = 1
        count -=1
        arimo.pop()
    else:
        ilikia.append(age)
    while  i < 1:
        g = input("give gender ")
        if g != "a" and g !="g":
            print("give rong gender ")  
        else:
            gcount += 1
            i +=1
            gen.append(g)
            TYPOS_EMB(age, amka) 

      


bubblesort (ilikia, arimo, gen)

print(ilikia)
print(arimo)
print(gen)


print("the women are ", (gcount))