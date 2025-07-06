# Programa que converte os segundos em horas, minutos e segundos.

segundos = int(input("Digite a quantidade de segundos: "))

minutos = segundos // 60
restosegundos = segundos % 60
horas = minutos // 60
restominutos = minutos % 60
 
print(horas, "horas ", restominutos, "minutos e ", restosegundos, "segundos.")