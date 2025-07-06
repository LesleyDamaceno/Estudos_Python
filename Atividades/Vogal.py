# Escreva a função vogal que recebe um único caractere 
# como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal (n):
	if (n == "a") or (n == "e") or (n == "i") or (n == "o") or (n == "u") or (n == "A") or (n == "E") or (n == "I") or (n == "O") or (n == "U"):
		resultado = True
	else:
		resultado = False
	return (resultado)

n = input("Digite um caracter: ")
while (len (n) > 1):
	n = input("Digite um caracter: ")
resposta = vogal (n)
print (resposta)