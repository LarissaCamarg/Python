from os import system 
from datetime import datetime, timedelta

def formata_valor(valor):
    return f'R$ {valor:.2f}'.replace('.',',').replace('_','.')

system('cls') 
try:
    capital= float(input('Capital inicial: '))
    taxa= float(input('Taxa de juros mensal: '))
    prazo= int(input('Quantidade de meses: '))
    montante= capital* (1 +taxa/100)**prazo
    hoje= datetime.now()
    vencimento= hoje + timedelta(days=30*prazo)
except ValueError:
    print('Valor incorreto. Por favor, tente novamente.')
else:
    print('\nResumo do investimento: ')
    print(f'Capital inicial:R$ {formata_valor(capital)} ')
    print(f'Taxa de juros:{taxa}% ao mês')
    print(f'Número de meses: {prazo} meses')
    print(f'\nMontante final: R$ {formata_valor(montante)}')
    print(f'Data de vencimento: {vencimento.strftime("%d/%m/%Y")}')

input('Digite enter para continuar...')
