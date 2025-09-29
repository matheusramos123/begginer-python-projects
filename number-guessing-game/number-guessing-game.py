# Foi gerado um import randint(Escolhe valores aleatórios, neste caso de 1 a 10)
from random import randint
palpite=0
maquina=randint(1,10)
# Enquanto o resultado não for o mesmo gerado pela máquina, o laço continuará, no momento em que é descoberto o número, o laço "quebra"
while True:
    while True:
        # Caso o usuário tente adicionar numeros diferentes de 1 a 10, o programa solicitará uma nova jogada, e não contabilizará no valor total de tentativas ao final. O laço é quebrado ao selecionar os números entre 1 e 10
        usuario=int(input('Advinhe o número da máquina!(1 a 10):'))
        if usuario < 1 or usuario > 10:
            print('Apenas aceitamos números inteiros')
        else:
            break
    # Condições foram adicionadas para facilitar e dinamizar o game, avisando se está errando por muito ou por pouco, estes avisos foram criados por condições "if", "elif", "else" 
    palpite+=1
    if usuario == maquina:
        print('Parabens, você ACERTOU!!!')
        break
    elif usuario > maquina:
        print('Experimente um número inferior...' )
    else: 
        print('Tente um valor mais alto!')
print(f'Foram necessários {palpite} palpites até você acertar!')
# Ao final é somado a quantidade de palpites que foram necessários com um contador que acrescente um a cada novo laço
