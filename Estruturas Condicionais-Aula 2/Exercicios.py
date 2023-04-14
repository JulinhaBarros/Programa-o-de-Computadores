# exercicio 1

pagamento = float(input ("Qual seu pagamento?"))
valor = pagamento
print ("seu salário é de", valor)

despesas = float(input ("Quanto você gastou no mês?") )
gastos = despesas
print ("você gastou no mês", gastos)

if (pagamento>despesas):
  print("A despesa está dentro do orçamento")
else :
  print("As despesas estão fora do orçamento")

#exercicio 2

numb = int( input("Insira um numero"))
if (numb % 2 == 0):
  print(numb, "é divisivel por 5")
else:
  print(numb, "não é divisivel por 5")


  #exercicio 3

numb = int( input("Digite um numero"))
print (numb % 2 == 0)
  
if(numb % 2 == 0):
   print('O número é par')
else:
   print ('O número é impar')


#exercicio 4

num = int(input("Digite um valor") )

numa = 20
numb = 30
numc = 40

total = (numa + numb + numc/3)

if(num % 2==0):
  print ( num,"é par")
  print (" A média aritimetica de a, b, c é",total)

if(num>10):
  calculo = ((numa*2) + (numb*3) + (numc*4))/ (2+3+4)
  print("A media ponderada é", calculo)


# exercicio 5

N1 = int( input(" Digite um valor inteiro"))
N2 = int( input(" Digite um valor inteiro"))
N3 = int( input(" Digite um valor inteiro"))

valores = (N1,N2,N3)
print(sorted (valores))