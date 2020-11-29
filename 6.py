cuv1=str(input("primul cuvint "))
cuv2=str(input("al doilea cuvint "))
cuv3=str(input("al treilea cuvint "))
cuv4=str(input("al patrulea cuvint "))
if len(cuv1)<3 or len(cuv2)<3 or len(cuv3)<3 or len(cuv4)<3:
    print("eroare")
else:
    cuv_nou=cuv1[0] + cuv2[0] + cuv3[0] + cuv3[1] + cuv3[2]
    for a in range(len(cuv4)//2):
        cuv_nou+=cuv4[a]
    print(f"cuvinte introduse: {cuv1}, {cuv2}, {cuv3}, {cuv4}")
    print("cuvintul nou ", cuv_nou)