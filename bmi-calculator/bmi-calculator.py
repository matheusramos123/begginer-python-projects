# Programa dentro do laço, dando sempre a opção ao usuário se ele quer ou não continuar com mais testes
while True:
    # Foi solicitado o peso e a altura para cálculo do IMC
    peso=float(input('Digite seu peso: '))
    altura=float(input('Digite sua altura: '))
    # Foi adicionado ao programa uma condição para aceitar apenas números positivos, evitando erro no sistema
    if peso==0 or altura==0:
        print('Peso e altura devem ser valores positivos!')
    else:
    # Condições do IMC geradas de acordo com a OMS
        imc=peso/(altura**2)
        print(f'Seu IMC é: {imc:.2f}')
        if imc < 16:
            print('Magreza Grau III!')
        elif (imc>=16) and (imc<=16.9):
            print('Magreza Grau II!')
        elif (imc>=17) and (imc<=18.4):
            print('Magreza Grau I!')
        elif (imc>=18.5) and (imc<=24.9):
            print('Eutrofia!')
        elif (imc>=25) and (imc<=29.9):
            print('Pré-obesidade!')
        elif (imc>=30) and (imc<=34.9):
            print('Obesidade moderada (Grau I)!')
        elif (imc>=35) and (imc<=39.9):
            print('Obesidade severa (Grau II)!')
        else:
            print('Obesidade muito severa (Grau III)!')
    # Caso o valor tenha sido diferente de 'S' OU 'N', o programa limita a resposta para apenas 'S' ou 'N', e retorna a pergunta
    while True:
            resp=str(input('Deseja continuar? (S/N): ')).upper()
            if resp in 'SN':
                break
            else:
                print('Apenas S para "Sim" e N para "Não"!')
    if resp == 'N':
        break
print('Programa encerrado!')
