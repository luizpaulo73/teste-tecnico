import json

with open("dados.json" , "r") as file:
    dados = json.load(file)


listaDias = []
for dia in dados:
    listaDias.append(dia["valor"])

while 0.0 in listaDias:
    listaDias.remove(0.0)

print(listaDias)

menorFaturamento = listaDias[0]
maiorFaturamento = listaDias[0]

for dia in listaDias:
    if dia < menorFaturamento:
        menorFaturamento = dia
    elif dia > maiorFaturamento:
        maiorFaturamento = dia

soma = 0
for dia in listaDias:
    soma += dia
media = soma / len(listaDias)

superouMediaMensal = 0
for dia in listaDias:
    if dia > media:
        superouMediaMensal += 1

print(f'''
    O menor faturamento foi de {menorFaturamento:.2f}
    O maior faturamento foi de {maiorFaturamento:.2f}
    A media de {media:.2f} foi ultrapassada em {superouMediaMensal} dias diferentes
    ''')