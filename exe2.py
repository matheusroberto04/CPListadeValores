print("""
    -----------------------------------
             CONSUMO VEÍCULO
    -----------------------------------
""")

#EX2
#Faça  um  programa  em  Python  que  leia  (carregue  via  teclado)  uma  lista  com  os modelos  de  cinco  carros  (exemplo  de  modelos:  FUSCA,  GOL,  VECTRA,  etc). Carregue   uma   outra   lista   com   o   consumo   desses   carros,   isto   é,   quantos quilômetros  cada  um  desses  carros  faz  com  um  litro  de  combustível


carros = []
consumo = []

for i in range(5):
    modelo = input(f"Digite o modelo do carro {i+1}: ")
    carros.append(modelo)
    
    consumo_km_litro = float(input(f"Digite o consumo do carro {modelo} (km/l): "))
    consumo.append(consumo_km_litro)

carro_economico = consumo.index(min(consumo))
mais_economico = carros[carro_economico]

distancia = 1000
custo_gasolina = 6.89
litros_utilizados = [distancia / consumo_carro for consumo_carro in consumo]
custo_total = sum(litros_utilizados) * custo_gasolina

print(f"Carro mais econômico: {mais_economico}")
print("Consumo para percorrer 1000 km:")
for i in range(5):
    print(f"{carros[i]}: {litros_utilizados[i]:.2f} litros")
    print(f"Custo total: R$ {custo_total:.2f}")




# Rm 551640 - Miguel Santos 
# Rm 98581 - Matheus Souza