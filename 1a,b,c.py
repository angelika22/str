sirul=str(input("dati sirul "))
majuscula=0
cifra=0
caracterele_speciale=0
for a in sirul:
    if ord(a) in range(65, 91):
        majuscula+=1
    if ord(a) in range(48, 58):
        cifra+=1
    if ord(a) in range(32, 48) or ord(a) in range(58, 65) or ord(a) in range(91, 97) or ord(a) in range(123, 127):
        caracterele_speciale+=1
print(f"a) numarul de majuscule in sir {majuscula}")
print(f"a) numarul de cifre in sir {cifra}")
print(f"a) numarul de caractere speciale in sir {caracterele_speciale}")
