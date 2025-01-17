def H10_to_H2(n):
    if n > 0:
        sd = n%2
        n = n//2
        H10_to_H2(n)
        print(sd,end =" ")

#Test case:
H10_to_H2(13)
print()
H10_to_H2(11)
print()
H10_to_H2(325)