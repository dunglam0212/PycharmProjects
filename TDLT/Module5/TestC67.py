i,j,k = 7,5,3

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =",i," j =",j," k=",k)