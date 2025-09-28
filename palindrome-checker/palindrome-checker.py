# Solicitei ao usuário que digitasse a palavra, foram inseridas condições para o programa revisar se era ou não um palíndromo!
palindromos=list()
while True:
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == palavra[::-1]:
        # Palíndromo: "diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa."
        print("É um palíndromo!")
        palindromos.append(palavra)
    else:
        print("Não é um palíndromo.")
    # Neste espaço foi colocado novamente um laço, só que agora com o objetivo de inspecionar 'resp' até que fosse constatado o uso da sigla 'S' ou 'N', encerrando o laço
    while True:
        resp=str(input('Deseja digitar mais uma palavra? (S/N)')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(f' Os palíndromos identificados foram: {palindromos}')
# Ao final, o programa agrupa em uma lista todos os palíndromos

    



