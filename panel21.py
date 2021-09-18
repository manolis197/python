def bubblesort (array, marray):
    n = len(array)

    for i in range (n-1):
        for j in range (0, n-i-1):
            if array[j] < array[j + 1] :
                array[j], array[j+1] = array[j + 1], array[j]
                marray[j], marray[j+1] = marray[j + 1], marray[j]
            elif array[j-1] == array[j]:
                if marray[j-1] > marray[j]:
                    marray[j-1], marray[j] = marray[j], marray[j-1]

omades = []
bathmi = []

prok = []
bathprok =[]

for i in range (5):
    t = input("give team name ")
    omades.append(t)

    b = input("dose bamo ")
    bathmi.append(b)

    if int(b) >= 5:
        prok.append(t)
        bathprok.append(b)


bubblesort(bathprok, prok)

print(bathprok)
print(prok)

N = len(bathprok)

pl = 0
for x in range (N):
    if bathprok[x] == bathprok[0]:
        pl +=1

print (pl)