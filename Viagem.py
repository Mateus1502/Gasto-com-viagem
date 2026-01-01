distancia = float(input("Informe a distância em km:"))
tempo = float(input("Informe o tempo em horas:"))
consumomedio = int(input("Informe o consumo médio do seu carro:"))
preco = float(input("Informe o preço do combustível:"))
litros = distancia / consumomedio #Distância sendo dividida pelos litros por km do carro
gasto = preco * litros #Preco do litro vezes a quantidade de litros gastos na viagem
velocidade_media = distancia / tempo
print("Velocidade média:", round(velocidade_media, 2), "km/h")
print ("Litros necessários:",round (litros, 2))
print ("O gasto é de:",round (gasto, 2))
