cidades = ["Recife', 'olinda', 'jaboatão', 'cabo de santo agostinho"]

c = float(input("informe a temperatura em graus celsius: "))
f = ((c*9)/5)+32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

f = float(input("\n informe a temperatura em graus fahrenheit: "))
c = ((f-32)*5)/9
print('A temperatura de {}°F corresponde a {}°C!'.format(f, c))

c = float(input("\n Digite a temperatura em °C: "))
f = ((c*9)/5)+32
print('A temperatura atual na cidade do Recife é de {}°C ou  {}°F!'.format(c, f))

c = float(input("\n Digite a temperatura  em °C: "))
f = ((c*9)/5)+32
print('A temperatura atual na cidade de Olinda é de {}°C ou  {}°F!'.format(c, f))

c = float(input("\n Digite a temperatura em °C: "))
f = ((c*9)/5)+32
print('A temperatura atual na cidade de Jaboatão é de {}°C ou  {}°F!'.format(c, f))

c = float(input("\n Digite a temperatura em °C: "))
print('A temperatura atual na cidade do cabo de santo agostinho é de {}°C ou  {}°F!'.format(c, f))


for c in range(1, 5):
     print("\n quer fazer a conversão novamente?")
     c = int(input("Então Digite a temperatura em °C: "))
     f = ((c * 9) / 5) + 32
     print('A temperatura atual na cidade do Recife é de {}°C ou  {}°F!'.format(c, f))
print('Fim')

for l in range(1, 5):
     print("\n quer fazer a conversão novamente?")
     l = int(input("Então Digite a temperatura em °C: "))
     f = ((c * 9) / 5) + 32
     print('A temperatura atual na cidade de olinda é de {}°C ou  {}°F!'.format(l, f))
print('Fim')

for b in range(1, 5):
     print("\n quer fazer a conversão novamente?")
     b = int(input("Então Digite a temperatura em °C: "))
     f = ((c * 9) / 5) + 32
     print('A temperatura atual na cidade do jaboatão é de {}°C ou  {}°F!'.format(b, f))
print('Fim')

for u in range(1, 5):
     print("\n quer fazer a conversão novamente?")
     u = int(input("Então Digite a temperatura em °C: "))
     f = ((c * 9) / 5) + 32
     print('A temperatura atual na cidade do cabo de santo agostinho é de {}°C ou  {}°F!'.format(u, f))
print('Fim')
