resposta = int(input("Digite um numero:\n"))

a = 0
b = 1

listaFibonacci = [a]

while b <= resposta:
    listaFibonacci.append(b)
    
    proximo = a + b
    a = b
    b = proximo

print(listaFibonacci)
if resposta in listaFibonacci:
    print(f"O numero {resposta} esta presente na sequencia de fibonacci")
else:
    print(f"O numero {resposta} nao esta presente na sequencia de fibonacci")