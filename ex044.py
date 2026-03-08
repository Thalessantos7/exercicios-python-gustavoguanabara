""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros """
valor = float(input("Preço das compras: R$"))
pagamento = int(input("""-----FORMAS DE PAGAMENTO-----
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Sua opção: """))

match pagamento:
    case 1:
        novoValor = valor - (valor * 10 / 100)

        print(f"Sua compra com 10% de desconto fica R${novoValor:.2f}")
    case 2:
        novoValor = valor - (valor * 5 / 100)

        print(f"Sua compra com 5% de desconto fica R${novoValor:.2f}")
    case 3:
        valorParcelado = valor / 2

        print(f"Sua compra será parcelada em 2x de R${valorParcelado:.2f} SEM JUROS")
    case 4:
        parcelas = int(input("Quantas parcelas? "))
        valorComJuros = valor + (valor * 20 / 100)
        valorParcelado = valorComJuros / parcelas

        print(f"Sua compra será parcelada em {parcelas}x de R${valorParcelado:.2f} COM JUROS \nSua compra de R${valor:.2f} vai custar R${valorComJuros:.2f}")