import datetime
#Obter a data de nascimento informada pelo usuário
birth_date = input("Informe sua data de nascimento (dd mm yyyy): ")

#Converter input para datetime object
birth_date = datetime.datetime.strptime(birth_date, "%d, %m, %Y")

#Calcular a diferenca de tempo
difference = datetime.datetime.now() - birth_date

#Extrair informações
days = difference.days
months = days // 30
years = days // 365

#Imprimir resultados
print(f"Anos desde o nascimento: {years}")
print(f"Meses desde o nascimento: {months}")
print(f"Dias desde o nascimento: {days}")

print(f"Você tem {years}, {months}, {days}")
