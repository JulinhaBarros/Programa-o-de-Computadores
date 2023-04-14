# exercicio 1

mês = int (input("digite um numero") )
x = mês
if (x == 1):
  print("Janeiro tem 31 dias")
  
if (x == 2):
  print("Fevereiro tem 28 ou 29 dias")

if (x == 3):
  print("Março tem 31 dias")

if (x== 4):
  print ("Abril tem 30 dias")

if (x == 5):
  print("Maio tem 31 dias")

if (x == 6):
  print("Junho tem 30 dias")
  
if (x == 7):
  print ("Julho tem 31 dias")

if (x == 8):
  print ("Agosto tem 31 dias")

if (x == 9):
  print ("Setembro tem 30 dias")

if (x == 10):
  print ("Outubro tem 31 dias")

if (x == 11):
  print ("Novembro tem 30 dias")

if (x == 12):
  print ("Dezembro tem 31 dias")


#exercicio 2

for i in range (1, 101):
  if (i % 1 == 0):
   print(i)


#exercicio 3

num = int(input("Digite um numero natural"))

for i in range (1, num + 1):
  if ( num >= 1 ):
   print(i)


# exercicio 4

n0 = int ( input("Digite o valor de n") )
m1 = int ( input("Digite o valor de m [maior que n]"))

for i in range (n0, m1 + 1):
  if ( m1 > n0 ):
   print(i)


#exercicio 5

for f in range (100, -1, - 1):
   print(f)

# exercicio 6

for i in range (33,48):
  ch = chr(i)
  print("O valor de",ch,"é:",i)

  
# exercicio 7
  
for i in range(65,91):
  print("Caracter '%s' tem código ASCII %d"%(chr(i), i))

  
# exercicio 8

for i in range(97, 123):
  print("Caracter '%s' tem código ASCII %d"%(chr(i), i))  # %d é a tabela ASCII

  
# exercicio 9

texto = input("Digite uma string:")

if texto.isupper():    # texto.isupper para maiuscula
 print("Tudo maiusculo")
elif texto.islower():  # texto.islower para minuscula
 print("Tudo minusculo")
else:
  print("Misturado")  #usado quando se tem maiúcula e minúscula
