n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
n3 = int(input("Insira a terceira nota: "))
m= int((n1 + n2 + n3)/3)
print ("Sua média foi: ", m)
ma= int((n1 + n2*2 + n3*3 + m)/7)
print ("Sua média de aproveitamento foi: ", ma)
if ma >= 9:
    print ("Sua média é maior que 9")
if ma <= 4:
    print ("Sua média foi menor que 4")
if ma < 9:
    print("Sua média foi", ma)
