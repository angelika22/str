CNP=str(input("CNP personal "))
if len(CNP) == 13:
    a=0
    while (a != len(CNP)) and (ord(CNP[a]) in range(48, 59)): 
        a+=1
    if a == len(CNP):
        print("corect")
else:
    print("eroare")