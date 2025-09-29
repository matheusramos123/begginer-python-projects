# Valores das variáveis que foram usadas no programa e lista adicionada para guardar os dicionários
maisidade=0
Nmulheres=0
Nhomens=0
Nomemaisidade=''
Fmais18=0
s=0
pessoas=list()
# Solicita a quantidade de dados que querem inserir, o laço irá até (n)= quantidade de dados que deseja cadastrar.
# Um novo dicionário é acrescentado no inicio de cada novo dado e ao final é enviado para uma lista com todos os outros dados 
n=int(input('Quantos dados deseja cadastrar? '))
for c in range(1,n+1):
    dados=dict()
    dados['Nome']=str(input('nome: ')).title()
    dados['Idade']=int(input('idade: '))
    # Laço é criado para que o usuário não digite outros valores e o programa os guarde equivocadamente, apenas permitindo M ou F como resposta
    while True:
        dados['Genero']=str(input('sexo: (M/F) ')).upper()
        if dados['Genero'] in 'MF':
            break
        else:
            print('Apenas são aceitos (M) ou (F) como resposta!')
    pessoas.append(dados) 
    # Condições para detectar quantidade de homens cadastrados no programa, idade da pessoa mais velha e quantidade de mulheres acima de 18 anos cadastradas     
    if dados['Genero'] == 'M':
        Nhomens += 1
        s += dados['Idade']
    elif dados['Genero']=='F':
        Nmulheres = Nmulheres+1
    if dados['Idade'] > maisidade:
        maisidade = dados['Idade']
        Nomemaisidade = dados['Nome']
    if dados['Genero']=='F':
        if dados['Idade'] >= 18:
            Fmais18 = Fmais18+1
print('|===+===+===+===+===+=== Relatorio Final ===+===+===+===+===+===|')
if Nhomens > 0:
    mediaH=s/Nhomens
    print(f'A media de idade dos homens cadastrados é {mediaH:.2f} anos! ')
else:
    print('Nenhum homem cadastrado no programa!')
print(f'Foram cadastrados {Nhomens} homens e {Nmulheres} mulheres no cadastro inteligente!')
print(f'{Nomemaisidade} é a pessoa mais velha cadastrada! ')
print(f'Temos {Fmais18} mulheres com mais de 18 anos cadastradas! ')
print('|===+===+===+===+===+===+====+===+===+===+===+===+===+===+===+==|')

    






