def Pitagoras(co, ca):
    hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
    print(f"\nO valor da hipotenusa é: {hipotenusa}")

if __name__ == '__main__':
    while True:
        print('Calculando a Hipotenusa\n')
        
        co = float(input('Digite o valor do cateto oposto: '))
        ca = float(input('Digite o valor do cateto adjacente: '))
        
        Pitagoras(co, ca)

        continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo: \n')
        if (continua == 'q'):
            break