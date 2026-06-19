n = input("qual nome?")
s = input("qual sobrenome?")
print(n +" "+ s)


frase = input("digite uma frase:")
print(frase.count(" "))


print("seu nome é", n)
resto = ""
for letra in n:
    resto += letra
    print(resto)


numero = input("digite um numero:")
if len(numero) == 8:
    numero = "9" + numero
    print(numero[0:5] + "-" + numero[5:9])
elif len(numero) == 9:
    if numero[0] == "9":
        print(numero[0:5] + "-" + numero[5:9])
    else:
        print("numero invalido")


frase = input("digite uma frase:")
vogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
print("a frase tem", vogais, "vogais")
indiceVOGAIS = []
for i in range(len(frase)):
    if frase[i] in "aeiou":
        indiceVOGAIS.append(i)
print("os indices das vogais são:", indiceVOGAIS)