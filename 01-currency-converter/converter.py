# Solicita ao usuário o valor em reais (BRL) que deseja converter
real=float(input('Digite o valor que quer converter: R$'))
# Laço para garantir que o usuário escolha uma moeda válida (D para Dólar ou E para Euro)
while True:
    resp=str(input('Quer converter para qual moeda, Dólar ou Euro? D= Dólar E= Euro: ')).upper()
    if resp in 'DE':
        break
    else:
        print('Apenas serão aceitos (D) OU (E) como resposta!')
# Verifica a escolha do usuário e realiza a conversão com base em taxas fixas
if resp=='D':
    dolar=real/5.10
    print(f'R${real:.2f} convertido para Dólar é: {dolar:.2f} USD.')
else:
    euro=real/6.20
    print(f'R${real:.2f} convertido para Euro é: {euro:.2f} EUR.')
print('Conversão realizada com sucesso!')   
        
    



