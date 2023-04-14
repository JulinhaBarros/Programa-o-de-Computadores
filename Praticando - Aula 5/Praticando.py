#exercicio 1

x = 0

while (x < 10):
 print ("**********")
 x = x + 1

x = 1



#exercicio 2

for c in range (1, 5+1):
  print ("*"*c)


  
#exercício 3

for c in range (5, 0, -1):
  print ("*"*c)


#exercicio 4

num1 = float (input("digite um numero"))
num2 = float (input("digite outro numero"))
num3 = float (input("digite mais um numero"))


if num1 < num2 + num3 and num2 < num1 + num2:
  print ("Os valores acima podem formar um triângulo")
  if num1 == num2 == num3:
    print ("Equilátero")

  if num1 != num2 != num3 != num1:
    print("Escaleno")
  else:
    print ("Isósceles")

else:
  ("Os valores não podem formar um triângulo")


  
#exercicio 5

for i in range (1, 100 + 1):
  if (i % 2):
    print ("elefantes incomodam muita gente")
  else:
    print (i, "elefantes", "incomodam"*i, "muito mais")
    

  
