def calculo_imc(peso,altura):
    return (peso/altura**2)

peso= float(input('Digite seu peso: '))
altura= float(input('Digite sua altura: '))

print(f'O calculo é {calculo_imc(peso,altura):.2f}')
