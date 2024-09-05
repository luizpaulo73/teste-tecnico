faturamentoMensal = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "outros" : 19849.53
}

faturamentoTotal = 0
for estado, valor in faturamentoMensal.items():
    faturamentoTotal += valor

porcentagemSP = (faturamentoMensal["SP"]/faturamentoTotal) * 100
porcentagemRJ = (faturamentoMensal["RJ"]/faturamentoTotal) * 100
porcentagemMG = (faturamentoMensal["MG"]/faturamentoTotal) * 100
porcentagemES = (faturamentoMensal["ES"]/faturamentoTotal) * 100
porcentagemOutros = (faturamentoMensal["outros"]/faturamentoTotal) * 100

print(f'''
        Faturamento total = {faturamentoTotal}
        SP = {porcentagemSP:.2f}%
        RJ = {porcentagemRJ:.2f}%
        MG = {porcentagemMG:.2f}%
        ES = {porcentagemES:.2f}%
        Outros = {porcentagemOutros:.2f}%
        ''')