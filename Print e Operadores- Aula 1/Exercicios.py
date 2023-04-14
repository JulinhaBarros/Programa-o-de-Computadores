# exercicio 1
print("exercicio 1")
nome = input("digite seu nome")



#exercicio 2
print("exercicio 2")
print("É um prazer te conhecer, {}!" .format(nome) )



#exercicio 3
print("exercicio 3")
agua = input("quantos copos de agua você bebeu hoje:")
armazenar = agua



#exercicio 4
print("exercicio 4")
print("Seu nome é",("Julia"), "você bebeu hoje",  armazenar,"copos de agua hoje.") 



# exercicio 5
print("exercicio 5")
digitar1 = int( input ("digite um número: ") )
digitar2 = int( input("digite um número: ") )

num1 = digitar1 
num2 = digitar2

total1 = num1 + num2
print(total1)

total2 = num1 - num2
print(total2)

total3 = num1/num2
print(total3)

total4 = num1 * num2
print(total4)



#exercicio 6
print("exercicio 6")

valor1 = int( input("digite o comprimento do retângulo :") )
valor2 = int(input("digite a largura do retângulo:") )
totalvalores = valor2 * valor1
print("a área desse retângulo é", totalvalores, ".")



#exercicio 7
print("exercicio 7")

comprimento = int( input("digite o comprimento do triângulo"))
largura = int( input("digite a largura do triângulo") )
area = (largura * comprimento)/2
print("a área desse triângulo é", area, ".")



# exercicio 8
print("exercicio 8")

raio = int( input("digite o valor do raio: ") )
r = raio
print(r)

pi = 3.14
p = pi
print(p)

area1 = r * r
area2 = area1 * p
print(" a área dessa cirunferência é,", area2, ".")



# exercicio 9
print("exercicio 9")

peso = float( input("Qual é o seu peso?: (Kg) ") )
altura= float( input("Qual é sua altura?: (m)") )
imc = peso / (altura ** 2)
print("o IMC de", "Julia","é de {:.1f}" "." .format(imc))
