def calcule_area (base, altura):
    return (base*altura/2)
    
base= float(input('Digite o valor da base em cm: '))
altura= float(input('Digite a altura em cm: '))

print(f'O valor da base é {calcule_area ( base, altura):.2f}')
