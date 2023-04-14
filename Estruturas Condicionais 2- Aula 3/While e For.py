#while = enquanto. Rodará infinito até a variavel x mudar

x = 0
while (x < 5):
  print("oi gente")
  x = x + 1 #incremento

# Soma dos numeros impares até 10
while (x <10):
  print(x)
  x = x + 2

  # Soma dos valores de 1 a 5

soma = 0
x = 1 
while (x < 5):
 soma = soma + x
 print(x)
 x = x + 1
    
 print ("a soma dos valores é", soma)


for i in range (1, 100):
  if (i % 2 == 0):
   print(i)


mensagem = "boa noite"
buscar = "n"

for i in range (0, 9):
  if(mensagem [i]==buscar):
    print("encontrei")

  

    