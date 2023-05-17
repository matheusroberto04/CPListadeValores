print("""
    -------------------------------
           SALTO DOS ATLETAS
    -------------------------------
""")
# EXERCICIO 1
# Em uma competição de salto em distância, cada atleta tem direito a realizar cinco saltos.  O  resultado  do  atleta  será  determinado  pela  média  dos  cinco  valores alcançados. Crie um programa em Python que receba o nome do atleta e as cinco distâncias alcançadas por ele em seus saltos e depois informe o nome, os saltos e a  média  dos  saltos.  O  programa  deve  armazenar  os  valores  alcançados  em  cada salto  em  uma  sequência  e  ser  encerrado  quando  não  for  informado  o  nome  do atleta. Segue um exemplo de saída do programa: 

    # Atleta: Silvânia Costa
    # Primeiro Salto: 6.5
    # Segundo Salto: 6.1
    # Terceiro Salto: 6.2
    # Quarto Salto: 5.4
    # Quinto Salto: 5.3
    # Resultado final:
    # Atleta: Silvania Costa
    # Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    # Média dos saltos: 5.9 m

nome = input(" Atleta: ")

saltos = []

#for s in range(5):
    #salto = float(input(f"Informe o valor do salto {s+1}: "))
    #saltos.append(salto)

s1 = float(input("Salto 1: "))
s2 = float(input("Salto 2: "))
s3 = float(input("Salto 3: "))
s4 = float(input("Salto 4: "))
s5 = float(input("Salto 5: "))

saltos.append(s1)
saltos.append(s2)
saltos.append(s3)
saltos.append(s4)
saltos.append(s5)
print("Resultado Final: ")

print("Atleta:", nome)

print("Saltos:",saltos)

media = (s1 + s2 + s3 + s4 + s5) / 5
print("Média: ", media)

# Rm 551640 - Miguel Santos 
# Rm 98581 - Matheus Souza