nome = "Gabriel"
idade = 18 
altura = 1.80
print(nome, idade, altura)

print("---------------------------------")

a, b, c = 5, 3.5, "Hello"
print(a)
print(b)
print(c)

print("---------------------------------")

meuNome = "Gabriel"
minhaIdade = 18
meuEndereco = "Minha casa !!!"
print(meuNome)
print(minhaIdade)
print(meuEndereco)

print("---------------------------------")

PI = 3.14
GRAVIDADE = 9.8
print(PI)
print(GRAVIDADE)

print("---------------------------------")

v = 100
print(v)
v = "agora sou uma string"
print(v)

print("---------------------------------")

letraA = 10
FloatB = 22.2
ComplexC = 3j
print(letraA)
print(FloatB)
print(ComplexC)

print(type(letraA))
print(type(FloatB))
print(type(ComplexC))

print("---------------------------------")

n1 = 3
n2 = 256323890868
n3 = -100

print(type(n1))
print(type(n2))
print(type(n3))

print("---------------------------------")

num1 = 21.3
num2 = 2.8
num3 = -17.78

print(type(num1))
print(type(num2))
print(type(num3))

print("---------------------------------")

namber = 35e4

print(type(namber))
print(namber)

e = 3.8e-2

print(type(e))
print(e)

print("---------------------------------")

print(1.79e309)
print(1.8e308)

print("---------------------------------")

print(5e-324)
print(5e-325)

print("---------------------------------")

namber1 = 2 + 4j
namber2 = -3j
namber3 = complex(3,4)

print(type(namber1))
print(type(namber2))
print(type(namber3))

print("---------------------------------")

print(namber3.real)
print(namber3.imag)

print("---------------------------------")

x = complex(4,3)
y = complex(-1,4)
z = complex(2,3)

print(x + y)
print(x + 1)
print(x * y)
print(x * 2)

print("---------------------------------")

import cmath

print(cmath .phase(x))
print(cmath.phase(complex(-1.0, 0.0)))
print(cmath.phase(complex(-1.0, -0.0)))

print(cmath.pi)
print(cmath.e)

import random

print(random.randrange(1,100))

print("---------------------------------")

k = 3
i = 7.7
z = 4j

print(type(k))
print(type(i))
print(type(z))
print(complex(k))
print(float(k))
print(int(i))

print("---------------------------------")

print(0b01111111)
print(0o10)
print(0XFF)

print("---------------------------------")

print(ord('A'))
print(ord('X'))
print(ord('<'))

print("---------------------------------")

print(chr(65))
print(chr(88))
print(chr(60))
print(chr(28779))

print("---------------------------------")

print('bla bla bla blu blin bla bla blin blin blin')
print("banana com nescau e arroz é bom mesmo hein")
print("""copa do mundo esta logo no proximo mes, sera que o mundo estara preparado""")

print("---------------------------------")

print("Podemos usar aspas dentro das \"string\"")
print("Podemos usar aspas denro das \'string\'")

print("---------------------------------")

print("Dessa forma não há 'problema'")
print('Dessa forma não há "problema"')

print("---------------------------------")

s = "Rafael"
print(s[0])
print(s[-0])

print(s[5])
print(s[-1])

print("---------------------------------")

nome = "Jonh Von Neuman"
print(nome[5:12])
print(nome[::-1])

print("---------------------------------")

nome = " Meu nome é Gabriel Batista "
print(nome.strip())
print(len(nome))
print(nome.lower())
print(nome.upper())
print(nome.swapcase())
print(nome.title())
print(nome.replace("Gabriel", "Biel"))
print(nome.split("-"))

print("---------------------------------")

listaNome = ["Gabriel", "Fabio", "Erick", "Kimari", "Davi"]

print(', '.join(listaNome))
print('-' .join(listaNome))

print("---------------------------------")

list('aeiou')
print('|'.join('aeiou'))

print("---------------------------------")

print("Ra Ra Ra Ja Ja Ta".count("Ra"))

print("---------------------------------")

print("existencialismo".startswith("exist"))
print("existencialismo".startswith("ismo"))

print("---------------------------------")

print("existencialismo".endswith("exist"))
print("existencialismo".endswith("ismo"))

print("---------------------------------")

print("Amar, é encontrar a propria felicidade alheia".find("amar"))
print("Amar, é encontrar a propria felicidade alheia".find("é"))

print("---------------------------------")

print("xyz678".isalnum())
print("xyz678".isalnum())
print(' '.isalnum())

print("---------------------------------")

print("exemplo".isalpha())
print("exemplo 2".isalpha())

print("---------------------------------")

print("33".isdigit())
print("a33z".isdigit())
print(''.isdigit())

print("---------------------------------")

print('nome'.isidentifier())
print('nome2'.isidentifier())
print('2nome'.isidentifier())
print('nome#'.isidentifier())

print("---------------------------------")

from keyword import iskeyword

print(iskeyword("or"))
print(iskeyword("else"))
print(iskeyword("while"))
print(iskeyword("switch"))