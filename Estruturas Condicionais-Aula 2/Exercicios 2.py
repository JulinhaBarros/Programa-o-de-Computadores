#exercicio 1

palavra = "Eu Estou Aqui"
resultado = palavra [0] + palavra [3] + palavra [9]
print(resultado)


#exercicio 2

cpf = input("Digite seu cpf")
resultado = cpf [9]

if (resultado=="1"):
  print("Seu cpf é do DF, GO, MS, TO")

if (resultado=="2"):
  print("Seu cpf é da região norte")

if (resultado=="3"):
  print("Seu cpf é do CE,MA ou PI")

if (resultado=="4"):
  print("Seu cpf é de PE, RN, PB ou AL")

if (resultado=="5"):
  print("Seu cps é da BA ou SE")

if (resultado=="6"):
  print("Seu cpf é de MG")

if(resultado=="7"):
  print("Seu cpf é do RJ ou ES")

if (resultado=="8"):
  print("Seu cpf é de SP")

if (resultado=="9"):
  print("Seu cpf é da região sul")

  
#exercicio 3

numer = 123
result =(1**3) + (2**3) + (3**3)

if (result==123):
  print(numer, "é um numero de Armstrong")

else:
  print(numer,"não é um numero de Armstrong")